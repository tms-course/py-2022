from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=256, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['author', ]),
            models.Index(fields=['title', ]),
        ]

