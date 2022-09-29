"""
How to convert json object to django queryset
from .models import Movie
from django.http import JsonResponse


def move_list(request):
    movie = Movie.objects.all()  # python dictionary object
    data = {
        "movie": list(movie.values())
    }
    return JsonResponse(data)


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active,
    }
    return JsonResponse(data)

"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieSerializers


@api_view(['GET', 'POST'])
def move_list(request):
    queryset = Movie.objects.all()
    serializer = MovieSerializers(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    if request.method == "GET":
        queryset = Movie.objects.get(pk=pk)
        serializer = MovieSerializers(queryset)
        return Response(serializer.data)

    if request.method == "PUT":
        queryset = Movie.objects.get(pk=pk)
        serializer = MovieSerializers(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == "DELETE":
        queryset = Movie.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



