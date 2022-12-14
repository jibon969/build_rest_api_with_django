from django.db import models


class Snippet(models.Model):
    title = models.CharField(required=False, allow_blank=True, max_length=100)
    code = models.CharField(max_length=120)

    def __str__(self):
        return self.title
