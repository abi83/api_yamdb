from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Lidia, create your models here.


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
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.TextField(
        max_length=100,
    )
    year = models.IntegerField()
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        null=True,
        blank=True
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
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    score = models.IntegerField(
        blank=True,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    text = models.TextField()
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        blank=True,
        null=False,
        related_name='reviews',
        default=0
        # TODO: А разве у нас может Ревью существовать без ссылки на Title?
    )

    class Meta:
        ordering = ['author']
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'],
                                    name='unique_review_title_author')
        ]


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
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
