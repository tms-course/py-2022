from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_feed, name='feed'),
    path('<int:id>/', views.redirect_to_blog, name='redirect_to_blog'),
    path('blogs/', include('blogs.urls'), name='blogs'),
]