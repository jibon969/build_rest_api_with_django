from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog, Category
from .serializers import CategorySerializer, BlogSerializer


class BlogList(APIView):
    """
    View to list all blog in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        queryset = Blog.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)
