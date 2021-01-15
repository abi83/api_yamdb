# Generated by Django 3.0.5 on 2021-01-15 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('title_api', '0019_auto_20210115_2350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['name', 'year']},
        ),
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(to='title_api.Genre'),
        ),
    ]