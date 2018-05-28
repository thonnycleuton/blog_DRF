from rest_framework import serializers

from post.models import Profile, Comment, Post, Geo, Address


class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):

    profile = serializers.SlugRelatedField(read_only=True, slug_field="name")
    count_comments = serializers.SerializerMethodField()

    def get_count_comments(self, obj):
        return obj.comment_set.count()

    class Meta:
        model = Post
        fields = ("url", "title", "body", "profile", "count_comments")


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ("id", "url", "name", "email", "address")


class ProfilePostsSerialiezer(serializers.ModelSerializer):

    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ("name", "email", "address", "posts")
