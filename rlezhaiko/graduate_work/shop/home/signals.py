from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import CustomerReview
from .tasks import send_email_task


@receiver(post_save, sender=CustomerReview)
def send_email(sender, instance, **kwargs):
    send_email_task.delay(instance.id, instance.status)