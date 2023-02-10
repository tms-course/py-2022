from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Blog
from .forms import PostCreationForm, PostSearchingForm


def show_feed(request):
    posts = Post.objects.exclude(status=Post.DRAFT)
    ctx = {
        'title': 'Feed',
        'posts': posts,
    }
    return render(request, 'feed.html', ctx)


def create_post(request, blog_id: int):
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            blog = get_object_or_404(Blog, pk=blog_id)
            post.blog = blog
            post.save()
            return redirect(f'/blogs/{blog.pk}/')
    else:
        form = PostCreationForm()

    ctx = {
        'form': form,
        'blog_id': blog_id
    }
    return render(request, 'create_post.html', ctx)


def redirect_to_blog(request, id: int):
    return redirect(f'/blogs/{id}/')


def publish_post(request, id: int):
    post = get_object_or_404(Post, pk=id)
    post.status = Post.PUBLISHED
    post.save()
    return redirect(f'show_my_blog', post.blog.pk)


def mark_post_as_deleted(request, id):
    post = get_object_or_404(Post, pk=id)
    post.status = Post.DELETED
    post.save()
    return redirect(f'show_my_blog', post.blog.pk)


def update_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostCreationForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('feed')

    else:
        form = PostCreationForm(instance=post)
    ctx = {
        'title': 'Update post',
        'form': form,
        'post': post
    }
    return render(request, 'update_post.html', ctx)


def search_post(request):
    if request.method == 'POST':
        form = PostSearchingForm(request.POST)
        if form.is_valid():
            posts = Post.objects.filter(title__contains=form.cleaned_data['post_title'])
            blogs = Blog.objects.filter(post__in=posts)
            return render(request, "list_blogs.html", {"blogs": blogs, 'title': 'Founded blogs'})
    else:
        form = PostSearchingForm()

    return render(request, 'search.html', {'form': form, 'title': 'Founded blogs'})
