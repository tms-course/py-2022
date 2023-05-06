from django.shortcuts import render, get_object_or_404

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


def get_product_by_slug(request, product_slug: str):
    category_all = Category.objects.all()
    product = get_object_or_404(Product, slug=product_slug)

    ctx = {
        'title': product.name,
        'shop_name': SHOP_NAME,
        'categories': list(category_all),
        'product': product,
    }

    return render(request, 'product_details.html', ctx)