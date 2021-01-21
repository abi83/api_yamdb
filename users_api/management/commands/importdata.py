import csv
import os

from _sqlite3 import IntegrityError
from django.core.management.base import BaseCommand

from users_api.models import YamdbUser
from title_api.models import Genre, Category
from title_api.models import Title, Comment, Review


class Command(BaseCommand):
    def handle(self, *args, **options):

        with open(os.getcwd() + '/data/users.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['bio'] = row.pop('description')

                obj, created = YamdbUser.objects.get_or_create(**row)
                if created:
                    obj.save()
                    print(f'{obj.__class__.__name__} object {obj} was created')

                else:
                    print(f'{obj.__class__.__name__} object {obj} already exists')

        with open(os.getcwd() + '/data/category.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                obj, created = Category.objects.get_or_create(**row)
                if created:
                    obj.save()
                    print(f'{obj.__class__.__name__} object {obj} was created')

                else:
                    print(f'{obj.__class__.__name__} object {obj} already exists')

        with open(os.getcwd() + '/data/genre.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                obj, created = Genre.objects.get_or_create(**row)
                if created:
                    obj.save()
                    print(f'{obj.__class__.__name__} object {obj} was created')

                else:
                    print(f'{obj.__class__.__name__} object {obj} already exists')

        with open(os.getcwd() + '/data/titles.csv', encoding='utf-8') as titles_file, open(os.getcwd() + '/data/genre_title.csv', encoding='utf-8') as gt_file:
            title_reader = csv.DictReader(titles_file)
            gt_reader = csv.DictReader(gt_file)
            for row in title_reader:
                gt_file.seek(0)
                genres = [g['genre_id'] for g in gt_reader if g['title_id'] ==row['id']]
                obj, created = Title.objects.get_or_create(
                    id=row['id'],
                    name=row['name'],
                    year=row['year'],
                    category=Category.objects.get(pk=row['category']),
                )
                if created:
                    obj.save()
                    print(f'{obj.__class__.__name__} object {obj} was created')
                    for g in Genre.objects.filter(pk__in=genres):
                        print(f'{g.__class__.__name__} object {g} was added to {obj}')
                        obj.genre.add(g)
                else:
                    print(f'{obj.__class__.__name__} object {obj} already exists')

        with open(os.getcwd() + '/data/review.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    obj, created = Review.objects.get_or_create(
                        id=row['id'],
                        author=YamdbUser.objects.get(pk=row['author']),
                        title=Title.objects.get(pk=row['title_id']),
                        score=row['score'],
                        text=row['text'],
                        pub_date=row['pub_date'],
                    )
                except Exception as e:
                    print(e)
                    created = False
                if created:
                    obj.save()
                    print(f'{obj.__class__.__name__} object {obj} was created')
                else:
                    print(f'{obj.__class__.__name__} object {obj} already exists')


        with open(os.getcwd() + '/data/comments.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                obj, created = Comment.objects.get_or_create(
                    id=row['id'],
                    review=Review.objects.get(pk=row['review_id']),
                    text=row['text'],
                    author=YamdbUser.objects.get(pk=row['author']),
                    pub_date=row['pub_date'],
                )
                if created:
                    obj.save()
                    print(f'{obj.__class__.__name__} object {obj} was created')
                else:
                    print(f'{obj.__class__.__name__} object {obj} already exists')
