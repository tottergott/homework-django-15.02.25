from django.contrib import admin

# Register your models here.
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...