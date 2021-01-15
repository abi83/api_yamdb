import django_filters
from django.shortcuts import render, get_object_or_404
from requests import Response
from rest_framework import viewsets, permissions, status
from rest_framework.templatetags.rest_framework import data

from title_api.models import Review, Comment, Title, Category, Genre
from title_api.permissions import AuthorPermissions
from title_api.serializers import ReviewSerializer, CommentSerializer, TitleSerializer, CategorySerializer


# Elena, create your views here.


# Lidia, create your views here.


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        AuthorPermissions
    ]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, ]

    def get_queryset(self):
        title_id = get_object_or_404(Review, pk=self.kwargs.get('title_id'))
        return Review.objects.filter(title=title_id)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        AuthorPermissions
    ]
    serializer_class = CommentSerializer

    def get_queryset(self):
        comment_obj = get_object_or_404(Review, pk=self.kwargs.get('review_id'), id=self.kwargs.get('review_id'))
        return Comment.objects.filter(comment=comment_obj)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        AuthorPermissions
    ]
    serializer_class = TitleSerializer
    queryset = Title.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        AuthorPermissions
    ]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        serializer.save(name=self.request.name)


class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        AuthorPermissions
    ]
    serializer_class = TitleSerializer
    queryset = Genre.objects.all()

