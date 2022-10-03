from django.contrib import admin
from .models import Movie, Award, Track, Album


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Movie


admin.site.register(Movie, MovieAdmin)


class AwardAdmin(admin.ModelAdmin):
    list_display = ['description']

    class Meta:
        model = Award


admin.site.register(Award, AwardAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_name']

    class Meta:
        model = Album


admin.site.register(Album, AlbumAdmin)


class TrackAdmin(admin.ModelAdmin):
    list_display = ['title']

    class Meta:
        model = Track


admin.site.register(Track, TrackAdmin)