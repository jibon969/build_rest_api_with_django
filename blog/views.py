from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination

from .models import Blog
from .serializers import BlogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class BlogList(APIView, LimitOffsetPagination):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        queryset = Blog.objects.all()
        results = self.paginate_queryset(queryset, request, view=self)
        serializer = BlogSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BlogSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BlogSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def bog_search(request):
    """
    In the brand list page users can search for a specific brand or related brand  with keywords.
    To get a search result you have to call this endpoint with a GET method request.

    :param request: https://belasea.com/products/api/brand-search/?title=beauty
    :return: brand-search data
    """

    query = request.query_params.get('query')
    if query:
        if query is not None:
            queryset = Blog.objects.all()
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(title__startswith=query) |
                Q(title__endswith=query)
            )
            serializers = BlogSerializer(queryset, many=True)
            return Response(serializers.data)
    else:
        return Response({"Search doesn't match, no data to show!"}, status=status.HTTP_404_NOT_FOUND)
