import django_filters
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, request

from title_api.models import Review, Comment, Title, Category, Genre
from title_api.permissions import AuthorPermissions
from title_api.serializers import ReviewSerializer, CommentSerializer, TitleSerializer, CategorySerializer


# Elena, create your views here.


# Lidia, create your views here.
from users_api.permissions import IsYamdbModerator, IsYamdbAdmin


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, AuthorPermissions
    ]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, ]

    def get_queryset(self):
        title_id = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return Review.objects.filter(title=title_id)

    def perform_create(self, serializer):
        title_id = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title_id)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        AuthorPermissions | IsYamdbAdmin | IsYamdbModerator
    ]
    serializer_class = CommentSerializer

    def get_queryset(self):
        title_id = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        review_id = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return Comment.objects.filter(title=title_id, review=review_id)

    def perform_create(self, serializer):
        title_id = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        review_id = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, title=title_id, review=review_id)


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
    serializer_class = TitleSerializer
    queryset = Title.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        AuthorPermissions
    ]
    serializer_class = TitleSerializer
    queryset = Genre.objects.all()