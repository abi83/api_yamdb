# Generated by Django 3.0.5 on 2021-01-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('title_api', '0003_auto_20210117_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, null=True, related_name='titles', to='title_api.Genre'),
        ),
    ]