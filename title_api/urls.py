from django.urls import path, include
from rest_framework.routers import DefaultRouter
from title_api.views import ReviewViewSet, CommentViewSet, TitleViewSet, CategoryViewSet

# Elena, create your urls here.


# Lidia, create your urls here.

router = DefaultRouter()

router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='review'
)
router.register('titles', TitleViewSet, basename='title')

router.register('categories', CategoryViewSet, basename='category')

router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comment'
)
urlpatterns = [
    path('v1/', include(router.urls))
]

