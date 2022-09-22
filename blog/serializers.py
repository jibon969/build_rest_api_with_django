from rest_framework import serializers
from .models import Category, Blog


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name'
        ]


class BlogSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField("get_category")

    class Meta:
        model = Blog
        fields = [
            'title', 'category', 'description'
        ]

    def get_category(self, obj):
        name = obj.category.name
        return name
