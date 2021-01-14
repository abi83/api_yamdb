from django.db import models

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class YamdbUser(models.Model):
    USER = 'usr', 'user'
    MODERATOR = 'mdr', 'moderator'
    ADMIN = 'adm', 'admin'
    CHOICES = (USER, MODERATOR, ADMIN)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=3, choices=CHOICES, default=USER)
