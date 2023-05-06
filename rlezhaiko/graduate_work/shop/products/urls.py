from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_product, name='product_list'),
    path('<slug:product_slug>/', views.get_product_by_slug, name='product_details_slug'),
]