from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Geo(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()


# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=50)
    suite = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    # geo = models.ForeignKey(Geo, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.street


class Profile(User):

    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'profiles'

    def __str__(self):
        return self.first_name


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    owner = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    postId = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name
