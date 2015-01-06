# Django Modules
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ System User
    """

    image = models.ImageField(
        upload_to='media/profiles/',
        blank=True,
        null=True
    )
