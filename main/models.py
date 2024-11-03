from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'static/avatar/{instance.username}/{filename}'


class User(AbstractUser):
    ava = models.ImageField(upload_to=user_directory_path)


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    time = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


# class PostTags(models.Model):
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.post.title + ': ' + self.tag.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, to_field='id')
    is_answer = models.BooleanField(default=False)
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.author.username + ': ' + self.text


class PostLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField()
