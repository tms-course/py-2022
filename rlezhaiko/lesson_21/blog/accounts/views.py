from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from blogs.models import Blog


def logout_user(request):
    logout(request)
    return redirect(reverse('blog_list'))


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(
                username=username, 
                password=raw_password)

            login(request, user)
            
            return redirect('blog_list')

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def user_list_blog(request):
    blogs = Blog.objects.filter(author=request.user)
    ctx = {'title': 'User blogs',
           'blogs': list(blogs),}
    return render(request, 'blog_list.html', ctx)


def user_list_post(request):
    blogs = Blog.objects.filter(author=request.user).all()
    all_user_posts = []
    for blog in blogs:
       all_user_posts.extend(list(blog.posts.all()))

    print(all_user_posts)
    ctx = {'title': 'User posts',
           'posts': all_user_posts,}
    return render(request, 'post_list.html', ctx)



