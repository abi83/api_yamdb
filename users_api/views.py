from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404


from users_api.models import YamdbUser
from users_api.serializers import UserSerializer, MeSerializer


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


class UserSelf(
    # viewsets.ViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
    # generics.RetrieveAPIView,
):
    serializer_class = MeSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'put', 'patch']
    queryset = YamdbUser.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_object(self):
        # breakpoint()
        return get_object_or_404(YamdbUser, username=self.request.user.username)
