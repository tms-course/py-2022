from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256, blank=False)
    description = models.CharField(max_length=256, blank=False)
    