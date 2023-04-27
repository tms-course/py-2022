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
