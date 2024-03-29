from django.contrib import admin
from django.urls import path
from . import views

# blogs
urlpatterns = [
    path('', views.list_blog, name='blog_list'),
    path('<int:id>/', views.get_blog_content, name='blog_content'),
]