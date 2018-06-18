from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_nested import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'profiles', ProfilesViewSet, base_name='profile')
router.register(r'posts', PostsViewSet, base_name='post')

urlpatterns = [
    url(r'^$', APIRoot.as_view(), name='root'),
    path('api-token-auth/', obtain_auth_token),
    path('api-token-auth2/', CustomAuthToken.as_view()),
]

urlpatterns += router.urls