from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Category, Post


def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
    }

    return render(
        request,
        'index.html',
        context
    )


def get_post(request, post_slug):
    post = Post.objects.filter(
        slug=post_slug,
    ).first()

    context = {
        'post': post,
    }

    return render(
        request,
        'post.html',
        context
    )

def get_category(request, category_slug):
    category = Category.objects.filter(
        slug=category_slug,
    ).first()
    posts = Post.objects.filter(category=category)
   
    context = {
        'category': category, 'posts': posts,
    }

    return render(
        request,
        'category.html',
        context
    )