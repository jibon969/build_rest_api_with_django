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
    award = MovieSerializers()

    class Meta:
        model = Award
        fields = [
            'award',
            'description',
        ]

    def create(self, validated_data):
        award_data = validated_data.pop('award')
        award_obj = Movie.objects.create(**validated_data)
        movie_obj = Award.objects.create(award=award_obj, **award_data)
        return movie_obj

    # def create(self, validated_data):
    #     awards_data = validated_data.pop('award')
    #     movie = Award.objects.create(**validated_data)
    #     for award_data in awards_data:
    #         Movie.objects.create(award=movie, **award_data)
    #     return movie

