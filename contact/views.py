from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactSerializer
from .models import Contact
from rest_framework.views import APIView


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


@api_view(['GET', 'PUT', 'DELETE'])
def contact_detail(request, pk):
    """
    Retrieve, update or delete a code contact.
    {
        "id": 3,
        "subject": "hi",
        "name": "SWE",
        "email": "jibon.belasea@gmail.com",
        "message": "test message"
    }
    
    """
    try:
        queryset = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ContactSerializer(queryset)
        context = {
            "results": serializer.data,
            "status": True,
            "message": "Your message successfully send !"
        }
        return Response(context)

    elif request.method == "PUT":
        serializer = ContactSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "results": serializer.data,
                "status": True,
                "message": "Update Successfully Complete !"
            }
            return Response(context)
        context = {
            "results": serializer.errors,
            "status": False,
            "message": "Cannot Successfully Complete !"
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        queryset.delete()
        context = {
            "status": True,
            "message": "Contact Successfully deleted !"
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)


class ContactList(APIView):
    """
    List all code Contact, or create a new contact.
    # Json Data format
    {
        "subject": "Hello, there",
        "name": "Jibon Ahmed",
        "email": "jayed.swe@gmail.com",
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
