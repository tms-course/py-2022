from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    telegram_user_id = models.IntegerField(blank=False)

    class Meta:
        indexes = [
            models.Index(fields=['user_id', 'telegram_user_id']),
        ]