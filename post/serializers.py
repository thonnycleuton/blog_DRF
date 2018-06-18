from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField

from .models import *


class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ("id", "url", "title", "body", "owner")


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ("id", "url", "username", "email", "posts")


class ProfilePostsSerialiezer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ("first_name", "email", "address", "posts")


class TotalSerializer(serializers.ModelSerializer):
    total_posts = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()

    def get_total_posts(self, obj):
        contador = obj.posts.count()
        return contador

    def get_total_comments(self, obj):
        contador = 0
        for post in obj.posts.all():
            contador += post.comments.all().count()
        return contador

    class Meta:
        model = Profile
        fields = ('pk', 'first_name', 'total_posts', 'total_comments')
