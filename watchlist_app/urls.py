from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('movie/', views.move_list),
    path('movie/<int:pk>/', views.movie_detail),

    path('award-list/', views.award_list),
    path('album-list/', views.album_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
