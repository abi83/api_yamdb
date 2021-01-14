from django.db import models
from django.contrib.auth.models import AbstractUser, Group

from django.contrib.auth import get_user_model
from django.db import models


class YamdbUser(AbstractUser):
    USER = 'usr', 'user'
    MODERATOR = 'mdr', 'moderator'
    ADMIN = 'adm', 'admin'
    CHOICES = (USER, MODERATOR, ADMIN)

    bio = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=3, choices=CHOICES, default=USER)
    # gr = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)