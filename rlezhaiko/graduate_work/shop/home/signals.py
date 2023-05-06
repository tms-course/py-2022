from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings

from .models import CustomerReview


@receiver(post_save, sender=CustomerReview)
def gen_slug_field(sender, instance, **kwargs):
    send_mail(
        'Review',
        f'You have 1 new review.\nhttp://127.0.0.1:8000/admin/home/customerreview/{instance.id}/change/',
        settings.EMAIL_HOST_USER,
        ['roman.lezhaiko@gmail.com'],
    )