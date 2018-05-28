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
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # geo = models.ForeignKey(Geo, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.street


class Profile(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    userId = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name
