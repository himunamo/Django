from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Shipping (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    landmark=models.CharField(max_length=100)
    Contact=models.CharField(max_length=10)
