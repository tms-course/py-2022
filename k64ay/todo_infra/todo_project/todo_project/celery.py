import os 

from celery import Celery
from dotenv import load_dotenv

infra_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(infra_dir, '.env'))

app = Celery('todo')

app.config_from_object('settings.celery')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.tasks.test_task',
        'schedule': 30.0,
        'args': ()
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

if __name__ == '__main__':
    app.start()