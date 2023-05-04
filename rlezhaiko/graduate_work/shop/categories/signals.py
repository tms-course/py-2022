from unidecode import unidecode

from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify

from .models import Category


@receiver(pre_save, sender=Category)
def gen_slug_field(sender, instance, **kwargs):
    instance.slug = slugify(unidecode(instance.name))
    print('Generated slug =', instance.slug)