# Generated by Django 3.0.5 on 2021-01-16 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('title_api', '0022_auto_20210116_1207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['author']},
        ),
    ]