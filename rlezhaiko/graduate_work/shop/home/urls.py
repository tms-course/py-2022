from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_home_page, name='home_page'),
    path('about_us/', views.get_about_us_page, name='about_us_page'),
    path('transport_services/', views.get_transport_services_page, name='transport_services_page'),
    path('mission_and_values/', views.get_mission_and_values_page, name='mission_and_values_page'),
    path('delivery/', views.get_delivery_page, name='delivery_page'),
    path('equipment_repair/', views.get_equipment_repair_page, name='equipment_repair_page'),
    path('replacement_and_return_products', views.get_replacement_and_return_products, name='replacement_and_return_products_page'),
    path('payment/', views.get_payment_page, name='payment_page'),
    path('contacts/', views.get_contacts_page, name='contacts_page'),
    path('customer_reviews/', views.get_customer_reviews_page, name='customer_reviews_page'),
    path('create_review/', views.create_review , name='review_create'),
]