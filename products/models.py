from django.db import models
from django.db.models.signals import post_save


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


def product_post_save_receiver(sender, instance, *args, **kwargs):
    obj = EntryList.objects.filter(product=instance)
    print("Obj :", obj)


post_save.connect(product_post_save_receiver, sender=Product)


class EntryList(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    last_purchase_price = models.DecimalField(default=0.0, max_digits=20, decimal_places=15)
    weight_avg_cost = models.DecimalField(default=0.0, max_digits=20, decimal_places=15)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)