from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home_page, name='home_page'),
    path('about_us/', views.get_about_us_page, name='about_us_page')
]