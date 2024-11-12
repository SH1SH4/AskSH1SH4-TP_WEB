from django.core.management.base import BaseCommand, CommandError
from main.models import Comment, Post, User
from random import choice, randint
from datetime import datetime


def create_comment_list(ratio):
    users = User.objects.all()
    posts = Post.objects.get_all()
    comments = [Comment(text='Пишу гадости', author=choice(users), post=choice(posts)) for _ in range(ratio)]
    return comments


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        comments = create_comment_list(kwargs['ratio'])
        Comment.objects.bulk_create(comments)

    def add_arguments(self, parser):
        parser.add_argument("-ratio", type=int)
