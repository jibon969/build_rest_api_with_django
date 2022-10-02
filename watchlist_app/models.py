from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


