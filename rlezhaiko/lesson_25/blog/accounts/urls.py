from django.urls import path, include

from . import views


urlpatterns = [
    path('logout', views.logout_user, name='logout_user'),
    path('register', views.register_user, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('blogs/', views.user_list_blog, name='user_blog_list'),
    path('posts/', views.user_list_post, name='user_post_list'),
]