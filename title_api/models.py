import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError

User = get_user_model()


class Category(models.Model):
    """Категории (типы) произведений"""
    name = models.CharField(max_length=200, verbose_name='category_title')
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True,
                            verbose_name='category_code')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(fields=['name'],
                                    name='unique_category')
        ]

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Жанры"""
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


def year_validator(value):
    if value < 1900 or value > datetime.datetime.now().year:
        raise ValidationError('It\'s is not a correct year!')


class Title(models.Model):
    """Заглавие"""
    name = models.TextField(
        max_length=100, db_index=True
    )

    year = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name='Year',
        validators=[year_validator]
    )
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['name', 'year']
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Review(models.Model):
    """Отзывы на произведения"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    score = models.IntegerField(
        blank=True,
        validators=[
            MaxValueValidator(10, 'Can\'t be more than 10'),
            MinValueValidator(1, 'Can\'t be less than 1')
        ]
    )
    text = models.TextField()
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        null=False,
        related_name='reviews',
        default=''
    )

    class Meta:
        ordering = ['pub_date']
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'],
                                    name='unique_review_title_author')
        ]


class Comment(models.Model):
    """Комментарии"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    review = models.ForeignKey(
        Review,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='comments',
        unique=False
    )
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['author']
