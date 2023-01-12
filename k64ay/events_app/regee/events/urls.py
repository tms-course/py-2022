from django.contrib import admin
from django.urls import path

from . import views

# /events/
urlpatterns = [
    path('', views.list_events, name='event_list'),
    path('create', views.create_event, name='create_event'),
    path('<int:event_id>', views.get_event, name='event_details'),
]