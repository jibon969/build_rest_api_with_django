from rest_framework import serializers
from .models import Movie, Award, Track, Album


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


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album