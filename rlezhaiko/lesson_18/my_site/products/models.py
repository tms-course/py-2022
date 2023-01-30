from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    