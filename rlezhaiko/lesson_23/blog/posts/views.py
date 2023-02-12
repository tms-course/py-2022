from django.shortcuts import render, redirect

from .models import Post
from blogs.models import Blog


def list_post(request):
    query = ''
    if request.method == 'POST':
        query = request.POST.get('search', '')
    
    posts = Post.objects.filter(status=Post.STATUS_PUBLISHED, title__contains=query) \
        | Post.objects.filter(status=Post.STATUS_PUBLISHED, blog__title__contains=query)

    ctx = {'title': 'All posts',
           'posts': list(posts),}
    return render(request, 'post_list.html', ctx)


def delete_post(request, post_id: int):
    post = Post.objects.filter(id=post_id)
    post.update(status=Post.STATUS_DELETED)
    return redirect('post_list')
