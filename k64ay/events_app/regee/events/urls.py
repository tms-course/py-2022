from django.contrib import admin
from django.urls import path

from . import views

# /events/
urlpatterns = [
    path('', views.list_events, name='event_list'),
]