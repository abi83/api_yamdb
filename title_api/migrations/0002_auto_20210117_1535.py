# Generated by Django 3.0.5 on 2021-01-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('title_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['author']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='title',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
