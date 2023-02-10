from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from django.db.transaction import set_autocommit, rollback, commit

from .models import Blog
from posts.models import Post


def list_blog(request):
    blogs = Blog.objects.all()
    ctx = {'title': 'All blogs',
           'blogs': list(blogs),}
    return render(request, 'blog_list.html', ctx)


def get_blog_content(request, id: int):
    try:
        blog = get_object_or_404(Blog, pk=id)
        posts = blog.posts.all()
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
    try:
        set_autocommit(False)
        Post.objects.filter(blog=blog_id).delete()
        Blog.objects.filter(id=blog_id).delete()
        commit()
    except:
        rollback()
        return HttpResponseNotFound('Bad request')
    
    return redirect('blog_list')