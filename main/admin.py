from django.contrib import admin
from main.models import *


# Register your models here.

@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
