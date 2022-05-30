from urllib.request import ProxyBasicAuthHandler
from django.db import models

# Create your models here.

class People(models.Model):
    name        = models.CharField  (max_length=50)
    price       = models.CharField  (max_length=50)
    nationality = models.CharField  (max_length=50)
    def __str__(self):
        return self.name


class Shoppingcart(models.Model):
    item = models.ForeignKey(People, on_delete=models.CASCADE)