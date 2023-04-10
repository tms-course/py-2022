import os

accept_content = ['json']

broker_url = os.environ.get('BROKER_REDIS_URL')

# Запускать celery задачи в основном патоке
task_always_eager = False
task_serializer = 'json'
task_default_queue = 'default'

# beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'