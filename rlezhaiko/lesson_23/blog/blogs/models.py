from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    STATUS_PUBLISHED = 0
    STATUS_DELETED = 1

    STATUS_CHOICES = [
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_DELETED, 'Deleted'),
    ]

    title = models.CharField(max_length=128, blank=False)
    theme = models.CharField(max_length=256, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_PUBLISHED)


    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['author']),
        ]