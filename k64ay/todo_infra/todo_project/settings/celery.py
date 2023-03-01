from importlib.util import find_spec
from os import environ

accept_content = ['json']

broker_url = environ["BROKER_REDIS_URL"]

task_always_eager = False
task_serializer = 'json'
task_track_started = True
task_send_sent_event = True
task_default_queue = 'default'
