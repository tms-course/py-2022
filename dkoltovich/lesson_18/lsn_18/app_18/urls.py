from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.index, name='index'),
    path('users/<int:id>/', views.update_user, name='update_user'),
    path('users/registration', views.register, name='register'),
]
