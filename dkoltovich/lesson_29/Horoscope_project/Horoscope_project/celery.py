from celery import Celery
from dotenv import load_dotenv
import os


horo_project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(horo_project_dir, '.env'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')

app = Celery('horo')
app.config_from_object('settings.celery')
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()