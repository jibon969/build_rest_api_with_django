from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet, Album, Track
from .serializers import SnippetSerializer, AlbumSerializer, TrackSerializer
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
        context = {
            "status": True,
            "message": "Get all Snippet list",
            "data": serializer.data
        }
        return JsonResponse(context, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "status": True,
                "message": "Successfully created new Snippet",
                "data": serializer.data
            }
            return JsonResponse(context, status=201)
        context = {
            "status": False,
            "message": "Successfully created new Snippet",
            "data": serializer.errors
        }
        return JsonResponse(context, status=400)


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


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        context = {
            "status": True,
            "message": "Get single snippet",
            "data": serializer.data
        }
        return JsonResponse(context, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "status": True,
                "message": "Get single snippet",
                "data": serializer.data
            }
            return JsonResponse(context, status=status.HTTP_201_CREATED)
        context = {
            "status": True,
            "message": "Get single snippet",
            "data": serializer.errors
        }
        return JsonResponse(context, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        snippet.delete()
        context = {
            "status": True,
            "message": "Get single snippet",
        }
        return HttpResponse(context, status=status.HTTP_204_NO_CONTENT)


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


class AlbumAPIView(APIView):

    def get(self, request):
        queryset = Album.objects.all()
        serializer = AlbumSerializer(queryset, many=True)
        context = {
            "status": True,
            "message": "Get all Album list",
            "data": serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request):
        """
        :param request:
        :return:
        """
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "status": True,
                "message": "Successfully created new Album",
                "data": serializer.data
            }
            return Response(context, status=status.HTTP_201_CREATED)
        else:
            context = {
                "status": False,
                "message": "Successfully created new Album",
                "data": serializer.errors
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

