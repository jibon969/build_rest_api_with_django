from rest_framework import serializers
from .models import Movie, Award


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'name',
            'description',
            'active'
        ]


class AwardSerializers(serializers.ModelSerializer):
    name = MovieSerializers()

    class Meta:
        model = Award
        fields = [
            'award',
            'description',
        ]

    def create(self, validated_data):
        award_data = validated_data.pop('award')
        award = Award.objects.create(**validated_data)
        movie_obj = Movie.objects.create(name=award, **award_data)
        return movie_obj
