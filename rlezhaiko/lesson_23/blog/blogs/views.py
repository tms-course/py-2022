from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from django.db import transaction

from .models import Blog
from posts.models import Post


def list_blog(request):
    blogs = Blog.objects.filter(status=Blog.STATUS_PUBLISHED)
    ctx = {'title': 'All blogs',
           'blogs': list(blogs),}
    return render(request, 'blog_list.html', ctx)


def get_blog_content(request, id: int):
    try:
        blog = get_object_or_404(Blog, pk=id)
        posts = blog.posts.filter(status=Post.STATUS_PUBLISHED)
        ctx = {'title': blog.title,
            'posts': list(posts),
            'blog_id': blog.id,
            'author': blog.author}
    except Blog.DoesNotExist:
        return HttpResponseNotFound
    return render(request, 'post_list.html', ctx)


def create_blog(request):
    if request.method == 'POST':
        blog = Blog(title=request.POST['title'], theme=request.POST['theme'], author=request.user)
        blog.save()
        return redirect('blog_list')
    return render(request, 'blog_create.html', {})


def create_post(request, id: int):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, pk=id)
        post = Post(title=request.POST['title'], content=request.POST['content'], blog=blog)
        post.save()
        return redirect('blog_content', id=id)
    return render(request, 'post_create.html', {})


def delete_blog(request, blog_id: int):    
    blog = Blog.objects.filter(id=blog_id)
    posts = Post.objects.filter(blog=blog_id, status=Post.STATUS_PUBLISHED)
    
    with transaction.atomic():
        blog.update(status=Blog.STATUS_DELETED)
        posts.update(status=Post.STATUS_DELETED)
    
    return redirect('blog_list')