from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from django.db import transaction
from django.views import View

from .models import Blog
from posts.models import Post
from .forms import BlogCreationForm
from posts.forms import PostCreationForm


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
        form = BlogCreationForm(request.POST)
        
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()

            return redirect('blog_list')
    else:
        form = BlogCreationForm()
    
    ctx = {'form': form}

    return render(request, 'blog_create.html', ctx)


def create_post(request, id: int):
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        
        if form.is_valid():
            # blog = get_object_or_404(Blog, pk=id)
            post = form.save(commit=False)
            post.blog = get_object_or_404(Blog, pk=id)
            post.save()

            return redirect('blog_content', id=id)
    else:
        form = PostCreationForm()
    
    ctx = {'form': form}

    return render(request, 'post_create.html', ctx)


class DeleteBlog(View):
    def post(self, request, blog_id: int):
        blog = Blog.objects.filter(id=blog_id)
        posts = Post.objects.filter(blog=blog_id, status=Post.STATUS_PUBLISHED)
        
        with transaction.atomic():
            blog.update(status=Blog.STATUS_DELETED)
            posts.update(status=Post.STATUS_DELETED)
        
        return redirect('blog_list')