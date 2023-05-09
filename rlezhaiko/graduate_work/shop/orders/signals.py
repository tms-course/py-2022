from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings

from .models import Order
from .tasks import send_email_task


@receiver(post_save, sender=Order)
def gen_slug_field(sender, instance, **kwargs):
    send_email_task.delay(instance.id)