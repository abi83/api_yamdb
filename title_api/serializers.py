from django.db.models import Avg
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from title_api.models import Review, Comment, Title, Category, Genre
from rest_framework.validators import UniqueValidator


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='title.name')
    author = serializers.ReadOnlyField(source='author.username')

    def validate(self, data):
        request = self.context.get('request')
        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if request.method != "PATCH" and Review.objects.filter(author=request.user, title=title).exists():
            raise serializers.ValidationError("Validation error. Review object with current author and title already "
                                              "exist!")
        return data

    class Meta:
        fields = ('id', 'title', 'text', 'author', 'score', 'pub_date',)
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    slug = serializers.SlugField(
        validators=[UniqueValidator(queryset=Category.objects.all())]
    )

    class Meta:
        fields = ('name', 'slug')
        model = Category
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    def validate(self, data):
        return data

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    rating = serializers.SerializerMethodField(source='get_rating')

    # category = CategorySerializer()
    # genre = GenreSerializer()

    def get_rating(self, obj):
        total_avg_rating = obj.reviews.aggregate(Avg('score'))
        return total_avg_rating.get('score__avg', 0)

    class Meta:
        fields = ('id', 'name', 'year', 'rating', 'description')
        model = Title
