from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


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
        context = {
            "status": False,
            "message": "Get all Snippet list",
            "data": serializer.data
        }
        return Response(context)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "status": False,
                "message": "Update Snippet",
                "data": serializer.data,
            }
            return Response(context)
        context = {
            "status": False,
            "message": "Not Update",
            "data": serializer.errors,
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        context = {
            "status": False,
            "message": "Delete Snippet",
        }
        snippet.delete()
        return Response(context, status=status.HTTP_204_NO_CONTENT)

