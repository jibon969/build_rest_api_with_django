from rest_framework import serializers
from .models import Category, Blog, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name'
        ]


class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    image = serializers.SerializerMethodField("get_image_url")

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'image', 'category', 'description', 'slug'
        ]

    def get_image_url(self, model):
        if model.image and hasattr(model.image, 'url'):
            return "http://127.0.0.1:8000" + model.image.url
            # return BASE_URL + model.image.url
        else:
            return "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/No_image_3x4.svg/1200px-No_image_3x4.svg.png"

    def create(self, validated_data):
        category = validated_data.pop("category")
        category_obj = Category.objects.create(**category)
        blog = Blog.objects.create(category=category_obj, **validated_data)
        return blog


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'author',
            'text',
            'approved_comment',
        ]

