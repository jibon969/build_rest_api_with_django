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
    category = CategorySerializer()
    image = serializers.SerializerMethodField("get_image_url")

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'image', 'category', 'description'
        ]

    def get_image_url(self, model):
        if model.image and hasattr(model.image, 'url'):
            return "http://127.0.0.1:8000" + model.image.url
            # return BASE_URL + model.image.url
        else:
            return "https://belasea.sgp1.digitaloceanspaces.com/static/images/logo/no-image-avalable.jpg"




