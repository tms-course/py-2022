from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from .models import Blog
import logging

LOGGER = logging.getLogger("Logger")
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

@receiver(post_save, sender=Blog)
def audit_log(sender, instance, **kwargs):
    LOGGER.info(f'{sender} {instance} was created')


@receiver(pre_save, sender=Blog)
def audit_log(sender, instance, **kwargs):
    LOGGER.info(f'{sender} {instance} ready to be created')

