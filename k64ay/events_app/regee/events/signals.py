from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from .models import Event

@receiver(request_finished)
def request_finished_cb(sender, **kwargs):
    print(_("Request finished!"), sender)


@receiver([pre_save, post_save], sender=Event)
def x_save_cb(sender, instance, **kwargs):
    print(sender)

@receiver([pre_save], sender=Event)
def gen_slug_field(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
    print('Generated slug =', instance.slug)