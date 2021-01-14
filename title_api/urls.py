from django.urls import path, include
from rest_framework.routers import DefaultRouter
from title_api.views import ReviewViewSet

# Elena, create your urls here.


# Lidia, create your urls here.

router = DefaultRouter()

router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)

urlpatterns = [
    path('v1/', include(router.urls))
]

