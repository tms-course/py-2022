import os

accept_content = ['json']

broker_url = os.environ.get('BROKER_REDIS_URL')

task_always_eager = False
task_serializer = 'json'
task_default_queue = 'default'