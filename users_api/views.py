from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from users_api.models import User
from users_api.serializers import UserSerializer


class CreateUser(viewsets.ViewSetMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView,):
    """
    Create user with POST request with email parameter.
    Wait for email confirmation code.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ConfirmUser(viewsets.ViewSetMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView,):
    """
    Activate your user with POST request included email and confirmation_code params
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersViewSet(viewsets.ViewSetMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   generics.GenericAPIView,):
    """
    Users List (for admin only), Send PATCH request to /api/v1/users/me/
    for editing your user information.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
