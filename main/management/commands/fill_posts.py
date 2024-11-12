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
    post_tags = []
    for i in range(0, ratio):
        post = Post(title=f'{i} - What is Lorem Ipsum?', text=TEXT, author=choice(users))
        posts.append(post)
        selected_tags = [choice(tags) for _ in range(randint(2, 5))]
        post_tags.append((post, selected_tags))
    return posts, post_tags


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        posts, post_tags = create_post_list(kwargs['ratio'])
        Post.objects.bulk_create(posts)
        for post, tags in post_tags:
            post_in_db = Post.objects.get(id=post.id)
            post_in_db.tags.set(tags)

    def add_arguments(self, parser):
        parser.add_argument("-ratio", type=int)
