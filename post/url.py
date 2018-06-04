from django.conf.urls import url
from rest_framework_nested import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'total', TotalViewSet, base_name='total')
router.register(r'profiles', ProfilesViewSet, base_name='profile')
router.register(r'profile-posts', ProfilePostViewSet, base_name='profile_posts')
router.register(r'address', ProfilePostViewSet, base_name='address')

profile_router = routers.NestedSimpleRouter(router, r'profiles', lookup='profile')
profile_router.register(r'posts', PostsViewSet, base_name='post')

post_router = routers.NestedSimpleRouter(profile_router, r'posts', lookup='post')
post_router.register(r'comments', CommentsViewSet, base_name='comment')

urlpatterns = [
    url(r'^$', APIRoot.as_view(), name='root'),
]

urlpatterns += router.urls
urlpatterns += profile_router.urls
urlpatterns += post_router.urls
for u in urlpatterns:
    print(u)
