from django.core.mail import send_mail
from django.conf import settings

from shop import celery_app


@celery_app.task(bind=True)
def send_email_task(self, instance_id, instance_status):
    if instance_status == 0:
        send_mail(
            'Review',
            f'You have 1 new review.\nhttp://127.0.0.1:8000/admin/home/customerreview/{instance_id}/change/',
            settings.EMAIL_HOST_USER,
            ['roman.lezhaiko@gmail.com'],
        )
        print('send by celery')