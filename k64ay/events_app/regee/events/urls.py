from django.contrib import admin
from django.urls import path

from . import views

# /events/
urlpatterns = [
    path('', views.list_events, name='event_list'),
    path('create', views.create_event, name='create_event'),
    path('<int:event_id>/', views.get_event_by_id, name='event_details_id'),
    path('<slug:event_slug>/', views.get_event_by_slug, name='event_details_slug'),
    path('<int:event_id>/delete/', views.delete_event, name='event_delete'),
    path('<int:event_id>/join/', views.join_event, name='join_event'),
]