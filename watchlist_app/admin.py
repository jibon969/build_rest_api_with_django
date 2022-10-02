from django.contrib import admin
from .models import Movie, Award


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