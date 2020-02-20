from shop.models import Product
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.product_name


class Cart(models.Model):
    # items = models.ManyToManyField(CartItem, blank=True)
    # products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    zip_code = models.CharField(max_length=1000)