from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

from .models import Question

@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")


@receiver([pre_save, post_save], sender=Question)
def update_question_signal(sender, instance, **kwargs):
    print(sender, instance, kwargs)