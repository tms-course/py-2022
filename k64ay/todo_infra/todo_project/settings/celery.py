import os

accept_content = ['json']

broker_url = os.environ.get('BROKER_REDIS_URL')
# Запускать celery задачи в основном потоке
task_always_eager = False
task_serializer = 'json'
task_default_queue = 'default'
