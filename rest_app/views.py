from django.http import Http404

from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class SnippetView(APIView):
    """
    # Example of Json Data
    {
        "title": "learn coding",
        "code" : "hello world"
    }
    """

    def get(self, request):
        """
        :param request:
        :return:
        """
        queryset = Snippet.objects.all()
        serializer = SnippetSerializer(queryset, many=True)
        context = {
            "status": True,
            "message": "Get all Snippet list",
            "data": serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request):
        """
        :param request:
        :return:
        """
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "status": True,
                "message": "Successfully created new Snippet",
                "data": serializer.data
            }
            return Response(context, status=status.HTTP_201_CREATED)
        else:
            context = {
                "status": False,
                "message": "Successfully created new Snippet",
                "data": serializer.errors
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)