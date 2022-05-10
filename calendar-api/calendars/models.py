from django.db import models

from account.models import User


class Calendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

