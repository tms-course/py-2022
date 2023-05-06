from unidecode import unidecode

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.core.mail import send_mail
from django.conf import settings

from .models import Product, ProductReview


@receiver(pre_save, sender=Product)
def gen_slug_field(sender, instance, **kwargs):
    instance.slug = slugify(unidecode(instance.name))


@receiver(post_save, sender=ProductReview)
def gen_slug_field(sender, instance, **kwargs):
    send_mail(
        'Review',
        f'You have 1 new review.\nhttp://127.0.0.1:8000/admin/products/productreview/{instance.id}/change/',
        settings.EMAIL_HOST_USER,
        ['roman.lezhaiko@gmail.com'],
    )