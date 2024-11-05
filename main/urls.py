from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ask', views.ask, name="ask"),
    path('question/<int:pk>/', views.question, name="question"),
    path('tag/<int:pk>/', views.tags_questions, name='tags_questions'),
    path('settings', views.settings, name='settings'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('hot/<int:pk>', views.hot, name="hot")
]
