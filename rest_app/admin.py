from django.contrib import admin
from .models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'code']

    class Meta:
        model = Snippet


admin.site.register(Snippet, SnippetAdmin)
