from django.shortcuts import render
from .models import Product


def list_product(request):
       products = Product.objects.all()
       ctx = {'title': 'Product list',
           'products': list(products),}
       return render(request, 'product_list.html', ctx)


def get_contact(request):
       return render(request, 'contact.html')


def about(request):
       return render(request, 'about.html')