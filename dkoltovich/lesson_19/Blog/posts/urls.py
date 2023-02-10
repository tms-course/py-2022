from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('', views.show_feed, name='feed'),
    path('publish/<int:id>/', views.publish_post, name='publish_post'),
    path('delete/<int:id>/', views.mark_post_as_deleted, name='mark_posts_as_deleted'),
    path('create/<int:blog_id>/', views.create_post, name='create_post'),
    path('update/<int:id>/', views.update_post, name='update_post'),
    path('<int:id>/', views.redirect_to_blog, name='redirect_to_blog'),
    path('blogs/', include('blogs.urls'), name='blogs'),
    path('search/', views.search_post, name='search_posts'),
]