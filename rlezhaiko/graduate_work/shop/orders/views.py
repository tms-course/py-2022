from django.shortcuts import render
from django.db import transaction

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from settings.base import SHOP_NAME


def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                order = form.save()
                print(order.items)
                for item in cart:
                    OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
                
            
            print(order.items.all())
            cart.clear()
            
            return render(request, 'created_order.html', {'order': order, 'shop_name': SHOP_NAME,})
    else:
        form = OrderCreateForm()
    
    return render(request, 'create_order.html', {'cart': cart, 'form': form, 'shop_name': SHOP_NAME,})