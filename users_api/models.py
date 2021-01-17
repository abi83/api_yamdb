from django.contrib.auth.models import AbstractUser

from django.db import models





class YamdbUser(AbstractUser):
    # class YamdbRole(models.Model):
    #     USER = 'U', 'user'
    #     MODERATOR = 'M', 'moderator'
    #     ADMIN = 'A', 'admin'
    #     CHOICES = [USER, MODERATOR, ADMIN]
    #
    #     name = models.CharField(max_length=1, choices=CHOICES)
    #
    #     def __str__(self):
    #         return 'self.name'

    USER = 'U', 'user'
    MODERATOR = 'M', 'moderator'
    ADMIN = 'A', 'admin'
    CHOICES = (USER, MODERATOR, ADMIN)

    bio = models.CharField(max_length=255, blank=True)
    _role = models.CharField(max_length=1, default=USER, choices=CHOICES)

    # def __init__(self, *args, **kwargs):
    #     mkwargs = {}
    #     for item, value in kwargs.items():
    #         if item != 'role':
    #             mkwargs[item] = value
    #     mkwargs['_role'] = kwargs.get('role') or self.USER
    #     super(YamdbUser, self).__init__(*args, **mkwargs)

    @property
    def role(self):
        return self._role
        # return str(self._role)[7:].split("'")[0]
    # role2 = models.CharField(max_length=1, choices=CHOICES2, default=USER2)

    # def get_role_display(self):
    #     if self.role:
    #         return 'RRole'
    #     return 'No role'
    #
    # def get_role(self):
    #     if self.role:
    #         return 'RRole'
    #     return 'No role'


    class Meta:
        ordering = ('-id',)


# DB Index
# email uniq
# USER_REGISTRATION = email
#

# django rest framework simple jwt!!!
# class: Token -> def for_user():
#
