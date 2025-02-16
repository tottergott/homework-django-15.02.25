from django.contrib import admin

from blog.models import Category, Post, Like, Comment, Donat

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Donat)
