from rest_framework import serializers
from title_api.models import Review

# Elena, create your serializers here


# Lidia, create your serializers here.

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review

