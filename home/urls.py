from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    path('home/', views.home, name="home"),
    path('student-list/', views.student_list),
    path('student-details/<int:pk>/', views.student_details),
]

urlpatterns = format_suffix_patterns(urlpatterns)
