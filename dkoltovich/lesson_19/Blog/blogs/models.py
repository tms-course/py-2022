from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    STATUS_DELETED = 0
    STATUS_ACTIVE = 1
    STATUS_CHOICES = (
        (STATUS_DELETED, 'Deleted'),
        (STATUS_ACTIVE, 'Active'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=256, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=STATUS_ACTIVE, choices=STATUS_CHOICES)

    class Meta:
        indexes = [
            models.Index(fields=['author', ]),
            models.Index(fields=['title', ]),
        ]

