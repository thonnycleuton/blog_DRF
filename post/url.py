from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'posts', PostsViewSet, base_name='post')
router.register(r'comments', CommentsViewSet, base_name='comment')
router.register(r'profiles', ProfileViewSet, base_name='profile')
router.register(r'profile-posts', ProfilePostViewSet, base_name='profile_posts')

urlpatterns = [
    url(r'^$', APIRoot.as_view(), name='root'),
]

urlpatterns += router.urls
for u in urlpatterns:
    print(u)
