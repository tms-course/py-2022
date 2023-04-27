from django.shortcuts import render

from categories.models import Category
from products.models import Product
from shop.settings import SHOP_NAME


def get_home_page(request):
    category = Category.objects.all()
    products = Product.objects.all()
    ctx = {'title': 'Главная',
           'name_header': 'name header',
           'name_footer': 'name footer',
           'categories': list(category),
           'products': list(products)
           }

    return render(request, 'home_page.html', ctx)


def get_about_us_page(request):
    count = Product.objects.count()
    ctx = {
        'count': count,
        'shop_name': SHOP_NAME
    }
    return render(request, 'about_us.html', ctx)


def get_transport_services_page(request):
    return render(request, 'transport_services.html', {'shop_name': SHOP_NAME})


def get_mission_and_values_page(request):
    return render(request, 'mission_and_values.html', {'shop_name': SHOP_NAME})


def get_delivery_page(request):
    return render(request, 'delivery.html', {'shop_name': SHOP_NAME})