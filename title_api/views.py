import django_filters
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters
from rest_framework import mixins
from rest_framework import generics


from title_api.models import Review, Comment, Title, Category, Genre
from title_api.permissions import AuthorPermissions
from title_api.serializers import ReviewSerializer, CommentSerializer, TitleSerializer, CategorySerializer
from users_api.permissions import IsYamdbModerator, IsYamdbAdmin, IsYamdbCategoryAdmin


# Elena, create your views here.


# Lidia, create your views here.


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [
        AuthorPermissions,
        permissions.IsAuthenticatedOrReadOnly,
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
        permissions.IsAuthenticatedOrReadOnly,  AuthorPermissions
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
    ]
    serializer_class = TitleSerializer
    queryset = Title.objects.all()

    def get_queryset(self):
        return Title.objects.annotate(
            rating=Avg('reviews__score')
        )


class CategoryViewSet(
    viewsets.ViewSetMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    permission_classes = [
        IsYamdbCategoryAdmin,
        # permissions.IsAuthenticatedOrReadOnly,
        # IsYamdbModerator,
    ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['=name', ]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'


class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        AuthorPermissions
    ]
    serializer_class = TitleSerializer
    queryset = Genre.objects.all()