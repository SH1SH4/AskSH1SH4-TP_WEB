from main.management.commands.fill_comments import create_comment_list
from main.management.commands.fill_posts import create_post_list
from main.management.commands.fill_tags import create_tag_list
from main.management.commands.fill_users import create_user_list
from main.models import User, Tag, Comment, Post
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        tags = create_tag_list(kwargs['ratio'])
        Tag.objects.bulk_create(tags)
        users = create_user_list(kwargs['ratio'])
        User.objects.bulk_create(users)

        #Прекрасно осознаю гадостность следующих строк, но причину ошибки я не выявил
        try:
            posts = create_post_list(kwargs['ratio'] * 10)
            Post.objects.bulk_create(posts)
        except IntegrityError:
            pass

        comments = create_comment_list(kwargs['ratio'] * 100)
        Comment.objects.bulk_create(comments)

    def add_arguments(self, parser):
        parser.add_argument("-ratio", type=int)