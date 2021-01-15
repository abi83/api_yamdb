import self as self
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
        related_name='posts'
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    score = models.IntegerField(
        blank=True,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    text = models.TextField()


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Category"
        ordering = ['name']

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=80)
    genre = models.CharField(max_length=80)
    year = models.IntegerField(
        'Год выпуска',
        db_index=True,
    )
    description = models.TextField(blank=True, null=True)
    categories = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles'
    )


class Genre(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

