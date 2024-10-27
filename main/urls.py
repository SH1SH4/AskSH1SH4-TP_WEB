from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ask', views.ask, name="ask"),
    path('question', views.question, name="question"),
    path('tag', views.tags_questions, name='tags_questions'),
    path('settings', views.settings, name='settings')
]
