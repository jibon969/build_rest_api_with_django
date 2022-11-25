from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializers


def home(request):
    return render(request, '')


@api_view(['GET', 'POST'])
def student_list(request):
    """
    List all code Award, or create a new Award.
    """
    if request.method == 'GET':
        queryset = Student.objects.all()
        serializer = StudentSerializers(queryset, many=True)
        context = {
            "status": True,
            "msg": "User successfully updated !",
            "results": serializer.data,
        }
        return Response(context)

    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def student_details(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        queryset = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializers(queryset)
        context = {
            "status": True,
            "msg": "Get Blog Data",
            "data": serializer.data,
        }
        return JsonResponse(context)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializers(queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "status": True,
                "msg": "PUT Blog Data",
                "data": serializer.data,
            }
            return JsonResponse(context)
        context = {
            "status": True,
            "msg": "Please try again !",
            "data": serializer.errors,
        }
        return JsonResponse(context, status=400)

    elif request.method == 'DELETE':
        queryset.delete()
        context = {
            "status": True,
            "msg": "Delete Blog Data",
        }
        return HttpResponse(context, status=204)
