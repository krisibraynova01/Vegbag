import uuid

from django.contrib.auth.models import User
from django.db import models

from vegbag.product.models import Product


# Create your models here.
class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)


class Cart(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, related_name='cart_item')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    STATUS = (
        (0, 'NEW'),
        (1, 'PROCESS'),
        (2, 'DELIVERED'),
        (3, 'CANCELLED'),
    )
    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=122)
    address = models.CharField(max_length=222)
    note = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

