from django.db import models

from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  related_name='products')
    keywords = models.CharField(max_length=512)
    description = models.TextField()
    attributes = models.JSONField()
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    main_image = models.ImageField(upload_to='static/images')
    slug = models.SlugField(max_length=128, blank=True, null=True, unique=True)


    def __str__(self) -> str:
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='static/images')
