from django.contrib import admin
from django.urls import path
from . import views

# posts
urlpatterns = [
    path('', views.list_post, name='post_list'),
    path('<int:post_id>/delete/', views.delete_post, name='post_delete'),
    path('search/', views.search_post, name='post_search'),
]