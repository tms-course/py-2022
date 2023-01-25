from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    organizer = models.ForeignKey(User, related_name="organizer", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=False)
    datetime = models.DateTimeField()
    location = models.CharField(max_length=256, blank=False)
    attendees = models.ManyToManyField(User, related_name='attendees')
    poster = models.ImageField(upload_to='events/images/', blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]
