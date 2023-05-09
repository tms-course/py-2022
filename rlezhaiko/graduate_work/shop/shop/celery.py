import os

from celery import Celery
from dotenv import load_dotenv

graduate_work_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(graduate_work_dir, '.env'))

app = Celery('shop')

app.config_from_object('settings.celery')
app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

if __name__ == '__main__':
    app.start()