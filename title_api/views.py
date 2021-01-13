import django_filters
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from title_api.models import Review
from title_api.permissions import AuthorPermissions
from title_api.serializers import ReviewSerializer

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

