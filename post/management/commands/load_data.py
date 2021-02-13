import json

from django.core.management import BaseCommand

from post.models import Profile, Address, Comment, Post

__author__ = 'Thonny Cleuton'


class Command(BaseCommand):

    def handle(self, **options):
        cont = 0
        dump_data = open('post/fixtures/db.json', 'r')
        dados = json.load(dump_data)

        for user in dados['users']:

            try:
                address = Address.objects.get_or_create(
                    street=user['address']['street'],
                    suite=user['address']['suite'],
                    zipcode=user['address']['zipcode'],
                    city=user['address']['city'])

                Profile.objects.get_or_create(
                    id=user['id'],
                    first_name=user['name'],
                    username=user['username'],
                    email=user['email'],
                    address=address[0])

            except Exception as e:
                print(e, cont)

        for posts in dados['posts']:
            try:
                Post.objects.get_or_create(
                    id=posts['id'],
                    title=posts['title'],
                    body=posts['body'],
                    owner=Profile.objects.get(id=posts['userId']))
            except Exception as e:
                print(e)

        for comment in dados['comments']:

            try:

                Comment.objects.get_or_create(
                    id=comment['id'],
                    name=comment['name'],
                    body=comment['body'],
                    email=comment['email'],
                    postId=Post.objects.get(id=comment['postId']))
            except Exception as e:
                print(e)
