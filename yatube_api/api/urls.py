from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet)
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
