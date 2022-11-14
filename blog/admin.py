from django.contrib import admin
from .models import Category, Blog, Comment


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


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_date', 'approved_comment']

    class Meta:
        model = Comment


admin.site.register(Comment, CommentAdmin)