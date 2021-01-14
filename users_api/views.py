from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from users_api.models import YamdbUser
from users_api.serializers import UserSerializer


class CreateUser(
    viewsets.ViewSetMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    """
    Create user with POST request with email parameter.
    Wait for email confirmation code.
    """
    queryset = YamdbUser.objects.all()
    serializer_class = UserSerializer


class ConfirmUser(viewsets.ViewSetMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView,):
    """
    Activate your user with POST request included email and confirmation_code params
    """
    queryset = YamdbUser.objects.all()
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
    queryset = YamdbUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsAdminUser,)

class UserSelf():
    pass