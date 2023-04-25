from django.db import models

from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name
