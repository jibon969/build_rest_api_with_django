from rest_framework import serializers
from .models import Movie, Award


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'id',
            'name',
            'description',
            'active'
        ]


class AwardSerializers(serializers.ModelSerializer):
    name = MovieSerializers()

    class Meta:
        model = Award
        fields = [
            'id',
            'name',
            'description',
        ]