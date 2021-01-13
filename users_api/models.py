from django.db import models

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Role(models.Model):
    class Roles(models.TextChoices):
        USER = 'usr', 'User'
        MODERATOR = 'mdr', 'Moderator'
        ADMIN = 'adm', 'Admin'
    name = models.CharField(max_length=3, choices=Roles.choices, default=Roles.USER)


class YamdbUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255,)
    role = models.ForeignKey(Role, on_delete=models.SET_DEFAULT, default=Role.Roles.USER)
