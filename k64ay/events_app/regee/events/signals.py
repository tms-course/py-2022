from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

from .models import Event

@receiver(request_finished)
def request_finished_cb(sender, **kwargs):
    print("Request finished!", sender)


@receiver([pre_save, post_save], sender=Event)
def x_save_cb(sender, instance, **kwargs):
    print(sender)