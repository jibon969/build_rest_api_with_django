from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('blog/', views.BlogList.as_view()),
    path('blog/<int:pk>/', views.BlogDetail.as_view()),
    path('blog/detail/<slug:slug>/', views.BlogDetailSlug.as_view()),
    path('blog-search/', views.bog_search),
    path('comment-list/', views.CommentList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
