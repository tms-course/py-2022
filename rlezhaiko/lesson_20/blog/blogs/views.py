from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Blog
from posts.models import Post


def list_blog(request):
    blogs = Blog.objects.all()
    ctx = {'title': 'Blogs',
           'blogs': list(blogs),}
    return render(request, 'blog_list.html', ctx)


def get_blog_content(request, id: int):
    try:
        blog = Blog.objects.get(id=id)
        posts = Post.objects.filter(blog__pk=id)
        ctx = {'title': blog.title,
            'posts': list(posts),}
    except:
        return HttpResponseNotFound
    return render(request, 'post_list.html', ctx)


def create_blog(request):
    if request.method == 'POST':
        blog = Blog(title=request.title, theme=request.theme, author=request.user)
        print(blog.__dict__)
    return render(request, 'blog_create.html', {})
