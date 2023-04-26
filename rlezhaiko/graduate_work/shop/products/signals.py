from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify

from .models import Product


@receiver(pre_save, sender=Product)
def gen_slug_field(sender, instance, **kwargs):
    instance.slug = slugify(instance.name, allow_unicode=True)
    print('Generated slug =', instance.slug)