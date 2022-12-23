from django.contrib import admin
from .models import Snippet, Album, Track


class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'code']

    class Meta:
        model = Snippet


admin.site.register(Snippet, SnippetAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_name', 'artist']

    class Meta:
        model = Album


admin.site.register(Album, AlbumAdmin)


class TrackAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration']

    class Meta:
        model = Track


admin.site.register(Track, TrackAdmin)