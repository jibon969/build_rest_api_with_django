from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'email']
    
    class Meta:
        model = Contact
        fields = [
            'title',
            'name',
            'email'
        ]


admin.site.register(Contact, ContactAdmin)
