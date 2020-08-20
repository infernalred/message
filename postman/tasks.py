import sys

from celery.utils.log import get_task_logger

from message.celery import app

from .service import check_email

logger = get_task_logger(__name__)


@app.task
def check_send_email(message, email, pk):
    print('Adding {0} + {1}'.format(message, email))
    logger.info("Start")
    check_email(message, email, pk)
