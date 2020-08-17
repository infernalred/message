from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Message(models.Model):
    email = models.EmailField(max_length=30)
    text = models.CharField(max_length=50)
    status = models.BooleanField(auto_created=False)
