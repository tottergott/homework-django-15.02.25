from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Category, Post


def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(
        request,
        'index.html',
        context
    )


def get_post(request, slug):
    post = Post.objects.filter(
        slug=slug,
    ).first()

    context = {
        'post': post,
    }

    return render(
        request,
        'post.html',
        context
    )