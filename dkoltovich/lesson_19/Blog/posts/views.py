from django.shortcuts import render, redirect
from .models import Post


def show_feed(request):
    posts = Post.objects.all()
    return render(request, 'feed.html', {'list': posts})


def redirect_to_blog(request, id: int):
    return redirect(f'/blogs/{id}/')
