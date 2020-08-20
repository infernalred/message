import logging
from smtplib import SMTPException

import requests
from django.conf import settings
from django.core.mail import send_mail

from postman.models import Postman

URL_USERS = "http://jsonplaceholder.typicode.com/users"


def send_message(message, check_user=None):
    send_mail(
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=settings.ADMIN_EMAIL,
        subject=message,
        message=check_user,
        fail_silently=False
    )


def check_email(message, email, pk):
    logging.info("Start task")
    connect_timeout, read_timeout = 5.0, 30.0
    try:
        resp = requests.get(URL_USERS, timeout=(connect_timeout, read_timeout)).json()
    except requests.ConnectionError:
        logging.error("Нет коннекта до сервера")
        raise ConnectionError("Ошибка подключения")
    search_p = [p for p in resp if p["email"] == email]
    try:
        send_message(message, str(search_p))
    except SMTPException as e:
        logging.error("There was an error sending an email: ", e)
        raise SMTPException("There was an error sending an email: ", e)
    email_db = Postman.objects.get(id=pk)
    email_db.sent = True
    email_db.save()
