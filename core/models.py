from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Owner(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

