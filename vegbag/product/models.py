from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=500)
    image = models.URLField()

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    rate_from_user = models.FloatField(default=0)
    description = models.TextField()
    product_image = models.URLField()
    is_discount = models.BooleanField()
    discount = models.IntegerField()

class Rate(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, name="rate_product")
    rate_of_product = models.IntegerField(
        choices=(
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
        )
    )
