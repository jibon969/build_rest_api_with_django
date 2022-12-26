from rest_framework import serializers
from .models import Snippet, Album, Track


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = [
            'id',
            'title',
            'code'
        ]


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = [
            'id',
            'album',
            'order',
            'title',
            'duration',
        ]


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ['id', 'album_name', 'artist', 'tracks']

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album



