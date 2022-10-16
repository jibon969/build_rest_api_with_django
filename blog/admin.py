from django.contrib import admin
from .models import Category, Blog


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title']

    class Meta:
        model = Blog


admin.site.register(Blog, BlogAdmin)
