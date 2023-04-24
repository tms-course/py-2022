from django.shortcuts import render


def list_product(request):
    ctx = {'title': 'All products',}
    return render(request, 'product_list.html', ctx)