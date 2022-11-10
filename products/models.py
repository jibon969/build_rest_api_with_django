from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=450)
    app_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0)
    weight = models.CharField(max_length=20, help_text='20ml/20gm', null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title