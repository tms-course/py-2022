from django.contrib import admin
from django.urls import path
from . import views

# posts
urlpatterns = [
    path('', views.list_post, name='post_list'),
]