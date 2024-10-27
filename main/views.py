from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def ask(request):
    return render(request, 'main/ask.html')


def question(request):
    return render(request, 'main/question.html')


def tags_questions(request):
    return render(request, 'main/tags_questions.html')


def settings(request):
    return render(request, 'main/settings.html')
