from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from main.models import *


def index(request):
    page_number = request.GET.get('page')
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_obj = paginator.get_page(page_number)

    last_page = paginator.page_range[-1]

    context = {
        'posts': page_obj,
        'last_page': last_page
    }
    return render(request, 'main/index.html', context=context)


def ask(request):
    return render(request, 'main/ask.html')


def question(request, pk):
    context = {
        'post': Post.objects.get(id=pk),
        'comments': Comment.objects.filter(post__id=pk).all(),
    }
    return render(request, 'main/question.html', context)


def tags_questions(request, pk):
    tag = Tag.objects.get(id=pk)
    posts = Post.objects.filter(tags=tag)
    page_number = request.GET.get('page')
    paginator = Paginator(posts, 3)
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj,
        'tag': tag.title
    }
    return render(request, 'main/tags_questions.html', context)


def settings(request):
    return render(request, 'main/settings.html')


def login(request):
    return render(request, 'main/login.html')


def register(request):
    return render(request, 'main/register.html')
