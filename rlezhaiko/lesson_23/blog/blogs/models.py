from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=128, blank=False)
    theme = models.CharField(max_length=256, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)


    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['author']),
        ]