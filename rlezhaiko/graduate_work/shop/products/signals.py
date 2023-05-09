from unidecode import unidecode

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

from .models import Product, ProductReview
from .tasks import send_email_task


@receiver(pre_save, sender=Product)
def gen_slug_field(sender, instance, **kwargs):
    instance.slug = slugify(unidecode(instance.name))


@receiver(post_save, sender=ProductReview)
def gen_slug_field(sender, instance, **kwargs):
    send_email_task.delay(instance.id, instance.status)