from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=120)
    dept = models.CharField(max_length=120)
    roll = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name