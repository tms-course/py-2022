from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    organizer = models.ForeignKey(User, related_name="organizer", on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=256,  blank=False)
    datetime = models.DateTimeField(_('Datetime'))
    location = models.CharField(_('Location'), max_length=256, blank=False)
    attendees = models.ManyToManyField(User, related_name='attendees')
    poster = models.ImageField(_('Poster'), upload_to='events/images/', blank=True)
    slug = models.SlugField(_('Slug'), max_length=256, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
        ]
