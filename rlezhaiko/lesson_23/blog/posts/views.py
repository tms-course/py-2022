from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Post
from blogs.models import Blog


def list_post(request):
    query = request.GET.get('search', '')
    posts = Post.objects.filter(Q(status=Post.STATUS_PUBLISHED), Q(title__contains=query) | Q(blog__title__contains=query))
    ctx = {'title': 'All posts',
           'posts': list(posts),}
    
    return render(request, 'post_list.html', ctx)


def delete_post(request, post_id: int):
    post = Post.objects.filter(id=post_id)
    post.update(status=Post.STATUS_DELETED)
    return redirect('post_list')
