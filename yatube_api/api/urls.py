from django.urls import include, path
from rest_framework import routers
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet)
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register('follow', FollowViewSet, basename='follow')

v1_patterns = [
    path('jwt/create/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
urlpatterns = [
    path('v1/', include(v1_patterns)),
]
