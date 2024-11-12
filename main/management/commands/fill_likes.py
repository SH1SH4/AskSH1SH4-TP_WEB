from django.core.management.base import BaseCommand, CommandError
from main.models import User, Comment, LikeComment
from random import choice, randint


def create_likes_list(ratio):
    users = User.objects.all()
    comments = Comment.objects.all()
    likes = []
    unique_pairs = set()

    while len(likes) < ratio:
        user = choice(users)
        comment = choice(comments)

        # Проверка на уникальность пары (user, comment)
        if (user.id, comment.id) not in unique_pairs:
            likes.append(LikeComment(user=user, comment=comment))
            unique_pairs.add((user.id, comment.id))

    return likes


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        likes = create_likes_list(kwargs['ratio'])
        LikeComment.objects.bulk_create(likes)

    def add_arguments(self, parser):
        parser.add_argument("-ratio", type=int)
