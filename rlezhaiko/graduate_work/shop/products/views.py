from django.shortcuts import render

from categories.models import Category
from .models import Product
from shop.settings import SHOP_NAME


def list_product(request):
    category = Category.objects.all()
    query = request.GET.get('search', '')
    products = Product.objects.filter(name__icontains=query)
    ctx = {'title': f'Результат поиска {query}',
           'shop_name': SHOP_NAME,
           'categories': list(category),
           'products': list(products)
           }
    
    return render(request, 'product_list.html', ctx)