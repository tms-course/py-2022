from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .models import Order
from shop import celery_app


@celery_app.task(bind=True)
def send_email_task(self, instance_id):
    order = Order.objects.get(id=instance_id)
    print(order.email)
    order_items = order.items.all()

    html_message = render_to_string('order_email.html', {'products': list(order_items), 'total_cost': order.get_total_cost()})

    send_mail(
        'Super-mega subject',
        'Email body text',
        settings.EMAIL_HOST_USER,
        ['roman.lezhaiko@gmail.com'],
        html_message=html_message,
    )