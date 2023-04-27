from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home_page, name='home_page'),
    path('about_us/', views.get_about_us_page, name='about_us_page'),
    path('transport_services/', views.get_transport_services_page, name='transport_services_page'),
    path('mission_and_values/', views.get_mission_and_values_page, name='mission_and_values_page'),
    path('delivery/', views.get_delivery_page, name='delivery_page')
]