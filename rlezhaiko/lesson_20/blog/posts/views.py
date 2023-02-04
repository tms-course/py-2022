from django.shortcuts import render
from .models import Post


def list_post(request):
    posts = Post.objects.all()
    ctx = {'title': 'Posts',
           'posts': list(posts),}
    return render(request, 'post_list.html', ctx)


def create_post(request):
    ctx = {'title': 'Create post',
           'blog_id': 0,}
    print(request)
    if request.method == 'POST':
        blog = Post(title=request.title, theme=request.theme, author=request.user)
        print(blog.__dict__)
    return render(request, 'post_create.html', {})
