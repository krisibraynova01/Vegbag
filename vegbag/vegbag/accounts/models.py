from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name="customer")
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)