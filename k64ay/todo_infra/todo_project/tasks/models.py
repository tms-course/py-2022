from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

