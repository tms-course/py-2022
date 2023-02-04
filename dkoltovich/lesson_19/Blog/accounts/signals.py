from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import logging

LOGGER = logging.getLogger("Logger")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


@receiver(post_save, sender=User)
def audit_log(sender, instance, **kwargs):
    LOGGER.info(f'{sender} {instance} was created')


@receiver(pre_save, sender=User)
def audit_log(sender, instance, **kwargs):
    logging.warning(f'{sender} {instance} ready to be created')

