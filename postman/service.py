import logging

import requests
from django.core.mail import mail_admins

from postman.models import Postman

URL_USERS = "http://jsonplaceholder.typicode.com/users"


def send_admins(message, check_user=None):
    mail_admins(
        subject=message,
        message=check_user,
        fail_silently=False
    )


def check_email(message, email, pk):
    try:
        resp = requests.get(URL_USERS).json()
    except requests.ConnectionError:
        logging.error("Нет коннекта до сервера")
        raise ConnectionError("Ошибка подключения")
    search_p = [p for p in resp if p["email"] == email]
    send_admins(message, str(search_p))
    email_db = Postman.objects.get(id=pk)
    email_db.sent = True
    email_db.text = "Отправлено"
    email_db.save()
    print(email_db.sent)
    # email_db = Postman.objects.filter(id=pk).update(sent=True)
    # print(email_db)
    # email_db.sent = "fsddfsfd"

