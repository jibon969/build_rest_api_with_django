from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('movie/', views.move_list),
    path('movie/<int:pk>/', views.movie_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
