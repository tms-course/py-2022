from django.shortcuts import render


def list_product(request):
    ctx = {'title': 'All products',
           'name_header': 'name header',
           'name_footer': 'name footer',
           }
    return render(request, 'product_list.html', ctx)