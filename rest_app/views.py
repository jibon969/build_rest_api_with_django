from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class SnippetView(APIView):
    """
    # Example of Json Data
    {
        "title": "learn coding",
        "code" : "hello world"
    }
    """

    def get(self, request):
        """
        :param request:
        :return:
        """
        queryset = Snippet.objects.all()
        serializer = SnippetSerializer(queryset, many=True)
        context = {
            "status": True,
            "message": "Get all Snippet list",
            "data": serializer.data

        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request):
        """
        :param request:
        :return:
        """
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "status": True,
                "message": "Successfully created new Snippet",
                "data": serializer.data

            }
            return Response(context, status=status.HTTP_201_CREATED)
        else:
            context = {
                "status": False,
                "message": "Successfully created new Snippet",
                "data": serializer.errors

            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
