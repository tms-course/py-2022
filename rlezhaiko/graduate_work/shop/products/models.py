from PIL import Image

from django.db import models
from django.contrib.auth.models import User

from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  related_name='products')
    keywords = models.CharField(max_length=512)
    description = models.TextField()
    attributes = models.JSONField()
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    main_image = models.ImageField(upload_to='static/images', blank=False)
    image_width = models.PositiveIntegerField(blank=False)
    image_height = models.PositiveIntegerField(blank=False)
    slug = models.SlugField(max_length=128, blank=True, null=True, unique=True)


    def __str__(self) -> str:
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='static/images', blank=False)
    image_width = models.PositiveIntegerField(blank=False)
    image_height = models.PositiveIntegerField(blank=False)
    

    # def save(self):
    #     super().save()  # saving image first

    #     img = Image.open(self.image.path) # Open image using self

    #     if img.height > 600 or img.width > 600:
    #         new_img = (600, 600)
    #         img.thumbnail(new_img)
    #         img.save(self.image.path)  # saving image at the same path


class ProductReview(models.Model):
    STATUS_DRAFT = 0
    STATUS_PUBLISHED = 1

    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_review = models.TextField('Отзыв', blank=False)
    admin_answer = models.TextField(blank=True)
    creation_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_DRAFT)


    class Meta:
        ordering = ["-creation_date"]


    def __str__(self) -> str:
        return self.product_review
