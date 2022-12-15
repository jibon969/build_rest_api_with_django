from django.urls import path
from . import views

urlpatterns = [
    path('snippet/', views.SnippetView.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]
