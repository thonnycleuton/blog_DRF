from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from post.models import Profile, Address, Comment, Post
from post.serializers import ProfileSerializer, PostSerializer, CommentSerializer, AddressSerializer, ProfilePostsSerialiezer


class ProfileViewSet(ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get']


class CommentsViewSet(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostsViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ProfilePostViewSet(ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfilePostsSerialiezer


class AddressViewSet(ModelViewSet):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class APIRoot(APIView):

    def get(self, request):

        data = {
            "profiles": "http://localhost:8000/profiles/",
            "posts": "http://localhost:8000/posts/",
            "comments": "http://localhost:8000/comments/",
            "profile_posts": "http://localhost:8000/profile-posts/",
        }

        return Response(data)
