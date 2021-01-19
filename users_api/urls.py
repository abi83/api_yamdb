from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include

from users_api.views import CreateUser, ConfirmUser, UsersViewSet, UserSelf

router = DefaultRouter()
# router.register(prefix='auth/email', viewset=CreateUser, basename='create-user')
# router.register(prefix='auth/token', viewset=ConfirmUser, basename='confirm-registration')
# router.register(prefix=r'^users/me$', viewset=UserSelf, basename='me')
router.register(prefix='users', viewset=UsersViewSet, basename='users')

urlpatterns = [
    path('v1/users/me/', UserSelf.as_view(), name='user-detail'),
    path('v1/', include(router.urls)),
]


urlpatterns += [
    path('v1/auth/email/', CreateUser.as_view(), name='user-registration'),
    path('v1/auth/token/', ConfirmUser.as_view(), name='confirm-user'),

]

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)


urlpatterns += [
    # path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('v1/token/refresh/', TokenRefreshView.as_view(),
    #      name='token_refresh'),
]
