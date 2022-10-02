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
from .models import Movie, Award
from .serializers import MovieSerializers, AwardSerializers


@api_view(['GET', 'POST'])
def move_list(request):
    """
    List all code Movie, or create a new Movie.
    """
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


@api_view(['GET'])
def award_list(request):
    """
    List all code Award, or create a new Award.
    """
    if request.method == 'GET':
        awards = Award.objects.all()
        serializer = AwardSerializers(awards, many=True)
        return Response(serializer.data)
