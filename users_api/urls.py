from rest_framework.routers import DefaultRouter
from django.urls import path, include

from users_api.views import CreateUser, ConfirmUser, UsersViewSet, UserSelf

router = DefaultRouter()
router.register(prefix='auth/email', viewset=CreateUser, basename='create-user')
router.register(prefix='auth/token', viewset=ConfirmUser, basename='confirm-registration')
router.register(prefix='users/me', viewset=UserSelf, basename='users')
router.register(prefix='users', viewset=UsersViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router.urls)),
]


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)

urlpatterns += [
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('v1/token/refresh/', TokenRefreshView.as_view(),
    #      name='token_refresh'),
]
