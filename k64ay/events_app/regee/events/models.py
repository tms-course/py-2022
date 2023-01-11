from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=256, blank=False)
    datetime = models.DateTimeField()
    location = models.CharField(max_length=256, blank=False)
    attendees = models.ManyToManyField(User)