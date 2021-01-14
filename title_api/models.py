from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Elena, create your models here


# Lidia, create your models here.

class Review(models.Model):

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    score = models.IntegerField(
        blank=True,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
     )
    text = models.TextField()

