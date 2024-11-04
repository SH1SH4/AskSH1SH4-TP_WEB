from django.core.management.base import BaseCommand, CommandError
from main.models import Tag, Post, User
from random import choice, randint

TEXT = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. " \
       "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s," \
       " when an unknown printer took a galley of type and scrambled it to make a type" \
       " specimen book. It has survived not only five centuries, but also the leap into" \
       " electronic typesetting, remaining essentially unchanged. It was popularised in" \
       " the 1960s with the release of Letraset sheets containing Lorem Ipsum passages," \
       " and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."


# Тут почему-то выдаёт ошибку, но код сам выполняется

def create_post_list(ratio):
    users = User.objects.all()
    tags = Tag.objects.get_all()
    posts = []
    for i in range(0, ratio):
        temp = Post.objects.create(title=f'{i} - What is Lorem Ipsum?', text=TEXT, author=choice(users))
        print(temp.id)
        temp.tags.add(*[choice(tags) for _ in range(randint(2,5))])
        posts.append(temp)
    return posts


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        posts = create_post_list(kwargs['ratio'])
        Post.objects.bulk_create(posts)

    def add_arguments(self, parser):
        parser.add_argument("-ratio", type=int)
