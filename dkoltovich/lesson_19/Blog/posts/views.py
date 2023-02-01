from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Blog
from .forms import PostCreationForm


def show_feed(request):
    posts = Post.objects.all()
    ctx = {
        'title': 'Feed',
        'posts': posts,
    }
    return render(request, 'feed.html', ctx)


def create_post(request):
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            blog = get_object_or_404(Blog, author=request.user)
            post.blog = blog
            post.save()
            return redirect(f'/blogs/{blog.pk}/')
    else:
        form = PostCreationForm
        return render(request, 'create_post.html', {'form': form})


def redirect_to_blog(request, id: int):
    return redirect(f'/blogs/{id}/')