from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from posts.models import Post
from .forms import BlogCreationForm


def list_blogs(request):
    blogs = Blog.objects.all()
    ctx = {
        'title': 'Blogs',
        'blogs': blogs
    }
    return render(request, 'list_blogs.html', ctx)


def create_blog(request):
    if request.method == 'POST':
        form = BlogCreationForm(request.POST)
        if form.is_valid():
            print('valid')
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return render(request, 'show_blog.html', {'title': 'Blog', 'blog': blog})

    form = BlogCreationForm
    return render(request, 'create_blog.html', {'title': 'Create blog', 'form': form})


def show_blog(request, id: int):
    try:
        blog = get_object_or_404(Blog, pk=id)
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


def show_my_blog(request):
    try:
        blog = get_object_or_404(Blog, author=request.user)
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