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

from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializers


def move_list(request):
    queryset = Movie.objects.all()
    serializer = MovieSerializers(queryset, many=True)
    return Response(serializer.data)

