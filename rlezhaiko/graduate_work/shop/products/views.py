from django.shortcuts import render

from categories.models import Category


def list_product(request):
    category = Category.objects.all()
    ctx = {'title': 'All products',
           'name_header': 'name header',
           'name_footer': 'name footer',
           'categories': list(category),
           }
    
    return render(request, 'product_list.html', ctx)