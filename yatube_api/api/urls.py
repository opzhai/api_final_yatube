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

jwt_patterns = [
    path('create/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('v1/jwt/', include(jwt_patterns)),
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
