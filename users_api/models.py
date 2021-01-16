from django.contrib.auth.models import AbstractUser

from django.db import models


class YamdbUser(AbstractUser):
    USER = 'usr', 'user'
    MODERATOR = 'mdr', 'moderator'
    ADMIN = 'adm', 'admin'
    CHOICES = (USER, MODERATOR, ADMIN)

    bio = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=3, choices=CHOICES, default=USER)

    class Meta:
        ordering = ('-id',)


# DB Index
# email uniq
# USER_REGISTRATION = email
#

# django rest framework simple jwt!!!
# class: Token -> def for_user():
#
