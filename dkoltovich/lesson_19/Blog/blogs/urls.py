from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_blogs, name='list_blogs'),
    path('<int:id>/', views.show_blog, name='show_blog'),
]