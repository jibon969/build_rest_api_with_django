from rest_framework import serializers
from .models import Contact


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'subject',
            'name',
            'email',
            'message',
        ]
