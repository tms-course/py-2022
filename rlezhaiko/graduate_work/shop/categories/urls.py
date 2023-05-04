from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_category_page, name='category_page'),
    path('<slug:category_slug>/', views.get_category_by_slug, name='category_details_slug'),
]