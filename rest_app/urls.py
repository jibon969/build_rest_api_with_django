from django.urls import path
from . import views

urlpatterns = [

    path('snippet/', views.SnippetView.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),

    path('snippet-list/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),

    path('album-list/', views.AlbumAPIView.as_view()),
    path('album/<int:pk>/', views.AlbumDetail.as_view()),

    path('track-list/', views.TrackAPIView.as_view()),
    path('track/<int:pk>/', views.TrackDetail.as_view()),
]
