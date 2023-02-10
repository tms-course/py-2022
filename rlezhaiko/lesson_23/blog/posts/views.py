from django.shortcuts import render, redirect

from .models import Post


def list_post(request):
    posts = Post.objects.all()
    ctx = {'title': 'All posts',
           'posts': list(posts),}
    return render(request, 'post_list.html', ctx)


def delete_post(request, post_id: int):
    Post.objects.filter(id=post_id).delete()

    return redirect('post_list')

def search_post(request):
    posts = Post.objects.filter(title__contains=request.POST['search'])
    ctx = {'title': f'Post by query: request.POST["search"]',
           'posts': list(posts),}
    return render(request, 'post_list.html', ctx)
