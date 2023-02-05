from django.shortcuts import render
from .models import Post


def list_post(request):
    posts = Post.objects.all()
    ctx = {'title': 'Posts',
           'posts': list(posts),}
    return render(request, 'post_list.html', ctx)