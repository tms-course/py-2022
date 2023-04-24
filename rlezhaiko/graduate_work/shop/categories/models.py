from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, blank=False)
    parent_id = models.IntegerField(null=True, blank=True)
    # slug = models.SlugField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, blank=True, null=True, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
        ]