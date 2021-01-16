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
        related_name='reviews'
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    score = models.IntegerField(
        blank=True,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    text = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id', 'author'],
                                    name='unique_review')
        ]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['author']


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(fields=['slug', 'name'],
                                    name='unique_category')
        ]

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=80)
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Title(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    genre = models.ManyToManyField(Genre)  # TODO: должен быть ManyToMany
    year = models.IntegerField(
        'Год выпуска',
        db_index=True,
    )
    # TODO: Год выпуска надо конечно надо ограничение,
    #  чтобы нельзя было меньше 1900 ввести и более 2030 скажем
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
        unique=False
    )

    class Meta:
        ordering = ['name', 'year']