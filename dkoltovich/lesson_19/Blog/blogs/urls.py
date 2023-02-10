from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_blogs, name='list_blogs'),
    path('create/', views.create_blog, name='create_blog'),
    path('mark_deleted', views.mark_blog_as_deleted, name='mark_blog_as_deleted'),
    path('<int:id>/', views.show_blog, name='show_blog'),
    path('my_blogs/', views.list_user_blogs, name='list_user_blogs'),
    path('my_blog/<int:id>/', views.show_my_blog, name='show_my_blog'),

]