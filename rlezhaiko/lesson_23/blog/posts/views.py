from django.shortcuts import render, redirect

from .models import Post
from blogs.models import Blog


def list_post(request):
    query = ''
    if request.method == 'POST':
        query = request.POST.get('search', '')
    
    posts = Post.objects.filter(status=Post.STATUS_PUBLISHED, title__contains=query)
    posts_all = Post.objects.filter(status=Post.STATUS_PUBLISHED)
    blogs_posts = []
    for post in list(posts_all):
        if query in post.blog.title:
            blogs_posts.append(post)
    
    blogs_posts.extend(list(posts))

    ctx = {'title': 'All posts',
           'posts': set(blogs_posts),}
    return render(request, 'post_list.html', ctx)


def delete_post(request, post_id: int):
    post = Post.objects.filter(id=post_id)
    post.update(status=Post.STATUS_DELETED)
    return redirect('post_list')
