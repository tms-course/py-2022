from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('', views.show_feed, name='feed'),
    path('<int:id>/', views.redirect_to_blog, name='redirect_to_blog'),
    path('<int:id>/publish/', views.publish_post, name='publish_post'),
    path('<int:id>/delete/', views.mark_post_as_deleted, name='mark_posts_as_deleted'),
    path('<int:blog_id>/create/', views.create_post, name='create_post'),
    path('<int:id>/update/', views.update_post, name='update_post'),
    path('blogs/', include('blogs.urls'), name='blogs'),
]