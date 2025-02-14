from django.contrib import admin

# Register your models here.
from .models import Category, Post , Likes, Comments


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...

@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):

    list_display = ('category', 'date', 'reaction')
    list_filter = ('category', 'date', 'reaction')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    ...