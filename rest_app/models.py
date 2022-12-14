from django.db import models


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=120)

    def __str__(self):
        return self.title
