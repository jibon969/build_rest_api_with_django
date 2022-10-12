from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('profile-list/', views.ProfileList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
