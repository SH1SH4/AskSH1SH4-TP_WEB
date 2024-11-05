from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db.models import Count


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'static/avatar/{instance.username}/{filename}'


class PostManager(models.Manager):
    def get_all(self):
        return self.all()

    def get_by_tag(self, tag):
        return self.filter(tags=tag)

    def get_one(self, pk):
        return self.get(id=pk)

    def get_hot(self):
        return self.annotate(comment_count=Count('comment')).order_by('-comment_count')


class TagManager(models.Manager):

    def get_one(self, pk):
        return self.get(id=pk)

    def get_all(self):
        return self.all()


class CommentManager(models.Manager):
    def get_one(self, pk):
        return self.get(id=pk)

    def get_all(self):
        return self.all()

    def get_most_liked(self, pk):
        return self.filter(post__id=pk).annotate(comment_count=Count('likecomment')).order_by('-comment_count')


class User(AbstractUser):
    ava = models.ImageField(upload_to=user_directory_path, default='static/avatar/default.jpg')

    def __str__(self):
        return f'{self.id}.{self.username}'


class Tag(models.Model):
    title = models.CharField(max_length=50)
    objects = TagManager()

    def __str__(self):
        return self.title


class Post(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    time = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    objects = PostManager()

    def __str__(self):
        return f'{self.id} {self.title}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, to_field='id')
    is_answer = models.BooleanField(default=False)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now())

    objects = CommentManager()

    def __str__(self):
        return f'{self.id} - {self.author.username}: {self.text}'


class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'comment')


class PostLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField()
