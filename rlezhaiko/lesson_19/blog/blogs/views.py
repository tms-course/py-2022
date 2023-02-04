from django.shortcuts import render, get_object_or_404
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
        blog = get_object_or_404(Blog, pk=id)
        posts = Post.objects.filter(blog__pk=id)
        ctx = {'title': blog.title,
            'posts': list(posts),}
    except Blog.DoesNotExist:
        return HttpResponseNotFound
    return render(request, 'post_list.html', ctx)
