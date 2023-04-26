from django.shortcuts import render

from categories.models import Category
from .models import Product


def list_product(request):
#     category = Category.objects.filter(name__exact='LG')
#     print(category[0].products.all())
#     ctx = {'title': 'All products',
#            'name_header': 'name header',
#            'name_footer': 'name footer',
#            'categories': list(category),
#            'products': 'list(products)'
#        }

    category = Category.objects.all()
    products = Product.objects.all()
    ctx = {'title': 'All products',
           'name_header': 'name header',
           'name_footer': 'name footer',
           'categories': list(category),
           'products': list(products)
           }
    

#     products = Product.objects.filter(category__name='LG')
#     ctx = {'title': 'All products',
#            'name_header': 'name header',
#            'name_footer': 'name footer',
#            'categories': list(category),
#            'products': list(products)
#            }


    return render(request, 'product_list.html', ctx)