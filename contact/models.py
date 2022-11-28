from django.db import models


class Contact(models.Model):
    subject = models.CharField(max_length=150)
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
