from rest_framework import serializers
from title_api.models import Review, Comment, Title, Category, Genre


# Elena, create your serializers here


# Lidia, create your serializers here.

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date',)
        model = Review

    def validate(self, data):
        """
        Болванка!!!!

        """
        # TODO: Мы должны получить из реквеста review и пользователя
        # TODO: проверить, что нет такого ревью у этого пользователя
        if self.context['request'].user == data.get('following'):
            raise serializers.ValidationError("You cant follow yourself")
        return data



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment


class TitleSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    rating = serializers.SerializerMethodField(source='get_rating')

    def get_rating(self, obj):
        # TODO: Получить obj (Title), получить все Review у данного Titile, высчитать
        # TODO: среднее арифмитическое из всех Review.score
        return 10

    class Meta:
        fields = ('id', 'name', 'year', 'rating',)
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
