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


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = [
            'id',
            'album_name',
            'artist'
        ]


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'id',
            'album',
            'order',
            'title',
            'duration',
        ]
