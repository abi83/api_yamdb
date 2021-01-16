from rest_framework import serializers
from title_api.models import Review, Comment, Title, Category, Genre


# Elena, create your serializers here


# Lidia, create your serializers here.

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment


class TitleSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        fields = ('id', 'name', 'year')
        model = Title


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        fields = ('name', 'slug')
        model = Genre
