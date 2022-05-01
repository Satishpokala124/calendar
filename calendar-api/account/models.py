from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


class MyUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not email:
            raise TypeError(f"'email' can't be None")
        if not password:
            raise TypeError(f"'password' can't be None")
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(
        _("email address"),
        unique=True, null=False,
        error_messages={
            "unique": _("A user with that email already exists."),
            "blank": _("Email can not be blank")
        }
    )
    objects = MyUserManager()
