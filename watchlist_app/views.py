from .models import Movie
from django.http import JsonResponse


def move_list(request):
    movie = Movie.objects.all()
    data = {
        "movie": movie
    }
    return JsonResponse(data)

