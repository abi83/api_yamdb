from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


from uuid import uuid1


class YamdbUserManager(BaseUserManager):
    def create_superuser(self, username=None, password=None, email=None):
        user_obj = self.create_user(
            username=str(uuid1()),
            email=email,
            password=password,
            is_staff=True,
            is_admin=True,
            is_active=True,
        )
        # user_obj.username = str(uuid1())
        return user_obj

    def create_user(self, email,
                    username,
                    password=None,
                    is_active=True,
                    is_staff=False,
                    is_admin=False,
                    ):
        if not username:
            raise ValueError("Unique username is required")
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("Password is required")
        user_obj = self.model(
            email=email
        )
        user_obj.set_password(password)
        user_obj.username = username
        user_obj.email = email
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj


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
    class Role(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'
        # CHOICES = (USER, MODERATOR, ADMIN)

    bio = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=10, default=Role.USER, choices=Role.choices)
    email = models.EmailField(unique=True, db_index=True, blank=False, null=False)
    # is_active = models.BooleanField(
    #     default=False,
    #     help_text='Designates whether this user should be treated as active. '
    #               'Unselect this instead of deleting accounts.',
    # )
    # password = models.Me
    username = models.CharField(unique=False, max_length=31)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # activation_code = models.CharField(max_length=40, blank=True, null=True)


    objects = YamdbUserManager()

@receiver(signals.post_save, sender=YamdbUser)
def send_code(sender, instance, created, **kwargs):
    code = default_token_generator.make_token(instance)
    if created:
        email = EmailMessage(
        'Confirmation code',
        f'Your confirmation code: {code}',
        'from@example.com',
        [f'{instance.email}', ],
        # ['bcc@example.com'],
        # reply_to=['another@example.com'],
        # headers={'Message-ID': 'foo'},
        )
        email.send()
    print('I am a reciever')
    print(f'Code: {code}')
    print(f'Sender: {sender}, instance: {instance}, created: {created}')

    # def __init__(self, *args, **kwargs):
    #     mkwargs = {}
    #     for item, value in kwargs.items():
    #         if item != 'role':
    #             mkwargs[item] = value
    #     mkwargs['_role'] = kwargs.get('role') or self.USER
    #     super(YamdbUser, self).__init__(*args, **mkwargs)

    # @property
    # def role(self):
    #     return self._role
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
