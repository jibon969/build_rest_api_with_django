from rest_framework import serializers
from .models import Category, Blog


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name'
        ]


class BlogSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField("get_category")
    image = serializers.SerializerMethodField("get_image_url")

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'image', 'category', 'description'
        ]

    def get_category(self, obj):
        name = obj.category.name
        return name

    def get_image_url(self, model):
        if model.image and hasattr(model.image, 'url'):
            return "http://127.0.0.1:8000" + model.image.url
            # return BASE_URL + model.image.url
        else:
            return "https://belasea.sgp1.digitaloceanspaces.com/static/images/logo/no-image-avalable.jpg"

    def create(self, validated_data):
        Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.category = validated_data.get('category', instance.category)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

