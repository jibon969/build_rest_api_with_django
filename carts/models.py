from django.db import models
from products.models import Product
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Entry(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    last_purchase_price = models.DecimalField(default=0.0, max_digits=20, decimal_places=15)
    weight_avg_cost = models.DecimalField( default=0.0, max_digits=20, decimal_places=15)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)