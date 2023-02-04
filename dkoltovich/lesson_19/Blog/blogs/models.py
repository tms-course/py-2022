from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=128, null=True, blank=True)

    creation_date = models.DateTimeField(auto_now=True)

