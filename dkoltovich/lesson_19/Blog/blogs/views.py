from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from posts.models import Post
from .forms import BlogCreationForm
from django.db import transaction

def list_blogs(request):
    blogs = Blog.objects.all()
    ctx = {
        'title': 'Blogs',
        'blogs': blogs
    }
    return render(request, 'list_blogs.html', ctx)


def show_blog(request, id: int):
    blog = get_object_or_404(Blog, pk=id)
    posts = Post.objects.filter(blog=blog)
    ctx = {
        'title': blog.title,
        'blog': blog,
        'posts': posts,
        'is_owner': blog.author == request.user
    }
    return render(request, 'show_blog.html', ctx)


@transaction.atomic()
def mark_blog_as_deleted(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blog.status = False
    posts = Post.objects.filter(blog=blog)
    posts.update(status=False)


def create_blog(request):
    if request.method == 'POST':
        form = BlogCreationForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('list_user_blogs')
    else:
        form = BlogCreationForm()

    ctx = {
        'title': 'Create blog',
        'form': form
    }
    return render(request, 'create_blog.html', ctx)


def list_user_blogs(request):
    blogs = Blog.objects.filter(author=request.user)
    if blogs.count() == 0:
        return redirect('create_blog')
    ctx = {
        'title': 'Blogs',
        'blogs': blogs
    }

    return render(request, 'list_blogs.html', ctx)


def show_my_blog(request, id):
    try:
        blog = Blog.objects.get(author=request.user, pk=id)
    except:
        return redirect('create_blog')
    posts = Post.objects.filter(blog=blog)
    ctx = {
        'title': blog.title,
        'blog': blog,
        'posts': posts,
        'is_owner': blog.author == request.user
    }
    return render(request, 'show_blog.html', ctx)