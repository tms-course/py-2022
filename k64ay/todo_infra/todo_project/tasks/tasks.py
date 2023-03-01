import time
import logging
from todo_project import celery_app

# Get an instance of a logger
logger = logging.getLogger(__name__)


@celery_app.task()
def callback(*args, **kwargs):
    time.sleep(10)
    logger.info('complete callback')

    return True
