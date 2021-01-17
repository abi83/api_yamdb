import csv
import os

from django.core.management.base import BaseCommand

from users_api.models import YamdbUser
from title_api.models import Genre, Category  # non relation models
from title_api.models import Title, Comment, Review  # models with relations. Genre-Title is the hardest!


class Command(BaseCommand):
    def handle(self, *args, **options):
        # import users
        with open(os.getcwd() + '/data/users.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['bio'] = row.pop('description')

                # role_convertor = {
                #     'user': YamdbUser.USER,
                #     'admin': YamdbUser.ADMIN,
                #     'moderator': YamdbUser.MODERATOR
                # }
                # for role in role_convertor:
                #     if row['role'] == role:
                #         row['role'] = role_convertor[role]

                obj, created = YamdbUser.objects.get_or_create(**row)
                if created:
                    obj.save()
                    print(f'User object {obj} was created')

                else:
                    print(f'User object {obj} already exists')

        # import categories
        with open(os.getcwd() + '/data/category.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                obj, created = Category.objects.get_or_create(**row)
                if created:
                    obj.save()
                    print(f'Category object {obj} was created')

                else:
                    print(f'Category object {obj} already exists')

        # import genres
        with open(os.getcwd() + '/data/genre.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                obj, created = Genre.objects.get_or_create(**row)
                if created:
                    obj.save()
                    print(f'Genre object {obj} was created')

                else:
                    print(f'Genre object {obj} already exists')


        with open(os.getcwd() + '/data/titles.csv', encoding='utf-8') as file:
            categories = Category.objects.all()
            reader = csv.DictReader(file)
            for row in reader:
                obj, created = Genre.objects.get_or_create(**row)
                breakpoint()
                if created:
                    obj.save()
                    print(f'Genre object {obj} was created')

                else:
                    print(f'Genre object {obj} already exists')

