from rest_framework.routers import DefaultRouter
from django.urls import path, include

from users_api.views import CreateUser, ConfirmUser, UsersViewSet

router = DefaultRouter()
router.register(prefix='auth/email', viewset=CreateUser, basename='create-user')
router.register(prefix='auth/token', viewset=ConfirmUser, basename='confirm-registration')
router.register(prefix='users', viewset=UsersViewSet, basename='users')
router.register(prefix='users/me', viewset=UsersViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router.urls)),
]
