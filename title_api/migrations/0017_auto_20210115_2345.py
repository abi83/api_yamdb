# Generated by Django 3.0.5 on 2021-01-15 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('title_api', '0016_auto_20210115_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]