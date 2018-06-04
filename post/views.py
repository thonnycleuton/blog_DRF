from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import *


class ProfilesViewSet(ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get']


class ProfileViewSet(ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CommentsViewSet(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(postId=self.kwargs['post_pk'])


class PostsViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(userId=self.kwargs['profile_pk'])


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
            "profile_posts": "http://localhost:8000/profile-posts/",
        }

        return Response(data)
