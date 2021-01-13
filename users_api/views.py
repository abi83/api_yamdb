from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from users_api.models import User
from users_api.serializers import UserSerializer
# Create your views here.


class CreateUser(viewsets.ViewSetMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView,):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ConfirmUser(viewsets.ViewSetMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView,):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersViewSet(viewsets.ViewSetMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   generics.GenericAPIView,):
    queryset = User.objects.all()
    serializer_class = UserSerializer
