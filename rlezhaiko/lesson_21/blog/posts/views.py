from django.shortcuts import render
from .models import Post
from blogs.models import Blog


def list_post(request):
    posts = Post.objects.all()
    ctx = {'title': 'All posts',
           'posts': list(posts),}
    return render(request, 'post_list.html', ctx)