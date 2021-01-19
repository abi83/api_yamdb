import django_filters
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets, permissions, filters
from rest_framework.viewsets import ViewSetMixin

from .filters import TitleFilter
from title_api.models import Review, Comment, Title, Category, Genre
from title_api.permissions import AuthorPermissions, IsAdminPermissions
from title_api.serializers import ReviewSerializer, CommentSerializer, TitlePostSerializer, TitleViewSerializer, CategorySerializer, \
    GenreSerializer
from users_api.permissions import IsYamdbCategoryAdmin


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        AuthorPermissions | IsAdminPermissions
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
        permissions.IsAuthenticatedOrReadOnly, AuthorPermissions
    ]
    serializer_class = CommentSerializer

    def get_queryset(self):
        review_id = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return Comment.objects.filter(review=review_id)

    def perform_create(self, serializer):
        review_id = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review_id)


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsYamdbCategoryAdmin
    ]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TitleViewSerializer
        return TitlePostSerializer

    def get_queryset(self):
        queryset = Title.objects.annotate(rating=Avg('reviews__score')).order_by('name', 'year')

        for param in ['genre', 'category', 'year', 'name']:
            param_query = self.request.query_params.get(param, None)
            kwarg_name = param

            if param == 'name':
                kwarg_name = f'{param}__contains'

            if param in ['genre', 'category']:
                kwarg_name = f'{param}__slug'

            if param_query is not None:
                return queryset.filter(**{f'{kwarg_name}': param_query})

        return queryset


class CategoryViewSet(
    viewsets.ViewSetMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [
        IsYamdbCategoryAdmin,
    ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['=name', ]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'


class GenreViewSet(ViewSetMixin,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView,
                   ):
    permission_classes = [
        IsYamdbCategoryAdmin,
    ]
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('name',)
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save()
