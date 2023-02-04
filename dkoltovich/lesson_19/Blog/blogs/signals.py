from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from .models import Blog
import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)


@receiver(post_save, sender=Blog)
def audit_log(sender, instance, **kwargs):
    logging.warning(f'{sender} {instance} was created')


@receiver(pre_save, sender=Blog)
def audit_log(sender, instance, **kwargs):
    logging.warning(f'{sender} {instance} ready to be created')

