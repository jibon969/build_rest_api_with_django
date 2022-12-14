from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class SnippetView(APIView):

    def get(self, request):
        queryset = Snippet.objects.all()
        serializer = SnippetSerializer(queryset, many=True)
        context = {
            "status": True,
            "serializer": serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)
