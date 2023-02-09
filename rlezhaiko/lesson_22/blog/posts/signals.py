import logging

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from .models import Post


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


@receiver(pre_save, sender=Post)
def pre_save(sender, instance, **kwargs):
    logging.debug(msg=f'{sender} - {instance} pre create')


@receiver(post_save, sender=Post)
def post_save(sender, instance, **kwargs):
    logging.debug(msg=f'{sender} - {instance} was created')