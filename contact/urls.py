from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('contact-list/', views.ContactList.as_view()),
    path('contact-detail/<int:pk>/', views.contact_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
