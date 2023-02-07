from django.shortcuts import render
from .models import Post
from blogs.models import Blog


def list_post(request):
    posts = Post.objects.all()
    ctx = {'title': 'All posts',
           'posts': list(posts),}
    return render(request, 'post_list.html', ctx)


def user_list_post(request):
    blogs = Blog.objects.filter(author=request.user).all()
    all_user_posts = []
    for blog in blogs:
       all_user_posts.extend(list(blog.posts.all()))

    print(all_user_posts)
    ctx = {'title': 'User posts',
           'posts': all_user_posts,}
    return render(request, 'post_list.html', ctx)