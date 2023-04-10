"""
WSGI config for Horoscope_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

horo_project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(horo_project_dir, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Horoscope_project.settings')

application = get_wsgi_application()
