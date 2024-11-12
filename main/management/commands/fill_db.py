from main.management.commands.fill_comments import create_comment_list
from main.management.commands.fill_posts import create_post_list
from main.management.commands.fill_tags import create_tag_list
from main.management.commands.fill_users import create_user_list
from main.management.commands.fill_likes import create_likes_list
from main.models import User, Tag, Comment, Post, LikeComment
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from time import time


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        start = time()
        tags = create_tag_list(kwargs['ratio'])
        Tag.objects.bulk_create(tags)
        users = create_user_list(kwargs['ratio'])
        User.objects.bulk_create(users)

        posts, post_tags = create_post_list(kwargs['ratio'] * 10)
        Post.objects.bulk_create(posts)
        for post, tags in post_tags:
            post_in_db = Post.objects.get(id=post.id)
            post_in_db.tags.set(tags)

        comments = create_comment_list(kwargs['ratio'] * 100)
        Comment.objects.bulk_create(comments)

        likes = create_likes_list(kwargs['ratio'] * 200)
        LikeComment.objects.bulk_create(likes)

        print(time() - start)

    def add_arguments(self, parser):
        parser.add_argument("-ratio", type=int)