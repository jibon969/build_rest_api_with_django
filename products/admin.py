from django.contrib import admin
from .models import Product, EntryList


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class EntryListAdmin(admin.ModelAdmin):
    list_display = ['id']

    class Meta:
        model = EntryList


admin.site.register(EntryList, EntryListAdmin)
