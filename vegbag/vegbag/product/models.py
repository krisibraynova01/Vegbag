from django.db import models


# Create your models here.
class Product(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rate_from_user = models.FloatField(default=0, null=True, blank=True)
    description = models.TextField()
    product_image = models.URLField()
    is_discount = models.BooleanField()
    discount = models.IntegerField(null=True, blank=True)

