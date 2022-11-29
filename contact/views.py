# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import ContactSerializer
# from .models import Contact
#
#
# @api_view(['GET', 'POST'])
# def contact_list(request):
#     """
#     List all code Contact, or create a new contact.
#     # Example of json files
#
#     {
#         "subject": "Hello",
#         "name": "SWE",
#         "email": "jibon.belasea@gmail.com",
#         "message": "test"
#     }
#     """
#     if request.method == 'GET':
#         snippets = Contact.objects.all()
#         serializer = ContactSerializer(snippets, many=True)
#         context = {
#             "data": serializer.data,
#             "status": True,
#             "msg": "Get all contact list"
#         }
#         return Response(context)
#
#     elif request.method == 'POST':
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             context = {
#                 "data": serializer.data,
#                 "status": True,
#                 "msg": "Your message successfully created !"
#             }
#             return Response(context, status=status.HTTP_201_CREATED)
#         context = {
#             "data": serializer.errors,
#             "status": False,
#             "msg": "Failed to insert new record"
#         }
#         return Response(context, status=status.HTTP_400_BAD_REQUEST)


from .models import Contact
from .serializers import ContactSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ContactList(APIView):
    """
    List all code Contact, or create a new contact.
    # Json Data format
    {
        "subject": "Hello, there",
        "name": "Jibon Ahmed",
        "email": "jibon.py@gmail.com",
        "message": "test message"
    }
    """

    def get(self, request, format=None):
        queryset = Contact.objects.all()
        serializer = ContactSerializer(queryset, many=True)
        context = {
            "data": serializer.data,
            "status": True,
            "msg": "Your message successfully created !",

        }
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "data": serializer.data,
                "status": True,
                "msg": "Your message successfully created !"
            }
            return Response(context, status=status.HTTP_201_CREATED)
        context = {
            "data": serializer.errors,
            "status": False,
            "msg": "Failed to insert new record"
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
