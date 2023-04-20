from django.db import models

# Create your models here.
class Event(models.Model):
    desc = models.CharField(max_length=512)
    user_id = models.IntegerField()