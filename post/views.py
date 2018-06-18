from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from post.permissions import IsOwnerOrReadOnly
from .serializers import *


class ProfilesViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get']
    permission_classes = (permissions.IsAuthenticated, )


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.profile)


class ProfilePostViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostsSerialiezer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class TotalViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = TotalSerializer


class APIRoot(APIView):

    def get(self, request):
        data = {
            "profiles": "http://localhost:8000/profiles/",
            "posts": "http://localhost:8000/posts/",
            "comments": "http://localhost:8000/comments/",
        }

        return Response(data)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'name': user.first_name,
        })
