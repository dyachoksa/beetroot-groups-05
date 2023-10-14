from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.order_by('-published_at').all()

    context = {"posts": posts}

    return render(request, "blog/index.html", context=context)


def show(request, slug):
    post = Post.objects.get(slug=slug)

    context = {"post": post}

    return render(request, 'blog/show.html', context=context)


def terms(request):
    return render(request, 'blog/terms.html')
