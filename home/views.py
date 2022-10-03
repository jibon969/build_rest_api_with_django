from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializers


@api_view(['GET', 'POST'])
def student_list(request):
    """
    List all code Award, or create a new Award.
    """
    if request.method == 'GET':
        queryset = Student.objects.all()
        serializer = StudentSerializers(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
