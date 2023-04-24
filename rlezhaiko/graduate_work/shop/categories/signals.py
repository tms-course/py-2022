from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify

from .models import Category


@receiver(pre_save, sender=Category)
def gen_slug_field(sender, instance, **kwargs):
    instance.slug = slugify(instance.name, allow_unicode=True)
    print('Generated slug =', instance.slug)