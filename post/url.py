from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_nested import routers

from . import views
from .views import *

router = routers.SimpleRouter()
router.register(r'profiles', ProfilesViewSet)
router.register(r'posts', PostsViewSet)
router.register(r'comments', CommentsViewSet)

urlpatterns = [
    url(r'api/', APIRoot.as_view(), name='root'),
    path('api-token-auth/', obtain_auth_token),
    path('api-token-auth2/', CustomAuthToken.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += router.urls
