from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_blogs, name='list_blogs'),
    path('create/', views.create_blog, name='create_blog'),
    path('<int:id>/', views.show_blog, name='show_blog'),
    path('my_blog', views.show_my_blog, name='show_my_blog'),
]