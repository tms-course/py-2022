from django.shortcuts import render

from categories.models import Category
from products.models import Product
from shop.settings import SHOP_NAME


def get_home_page(request):
    category = Category.objects.all()
    products = Product.objects.all()
    ctx = {'title': 'Главная',
           'shop_name': SHOP_NAME,
           'name_header': 'name header',
           'name_footer': 'name footer',
           'categories': list(category),
           'products': list(products)
           }

    return render(request, 'home_page.html', ctx)


def get_about_us_page(request):
    count = Product.objects.count()
    ctx = {'title': 'О нас',
           'count': count,
           'shop_name': SHOP_NAME
           }
    return render(request, 'about_us.html', ctx)


def get_transport_services_page(request):
    ctx = {'title': 'Транспортные услуги',
           'shop_name': SHOP_NAME
           }
    return render(request, 'transport_services.html', ctx)







def get_mission_and_values_page(request):
    ctx = {'title': 'Миссия и ценности',
           'shop_name': SHOP_NAME
           }
    return render(request, 'mission_and_values.html', ctx)


def get_delivery_page(request):
    ctx = {'title': 'Доставка',
           'shop_name': SHOP_NAME
           }
    return render(request, 'delivery.html', ctx)


def get_equipment_repair_page(request):
    ctx = {'title': 'Ремонт техники',
           'shop_name': SHOP_NAME
           }
    return render(request, 'equipment_repair.html', ctx)


def get_replacement_and_return_products(request):
    ctx = {'title': 'Замена и возврат товара',
           'shop_name': SHOP_NAME
           }
    return render(request, 'replacement_and_return_products.html', ctx)


def get_payment_page(request):
    ctx = {'title': 'Оплата',
           'shop_name': SHOP_NAME
           }
    return render(request, 'payment.html', ctx)


def get_contacts_page(request):
    ctx = {'title': 'Контакты',
           'shop_name': SHOP_NAME
           }
    return render(request, 'contacts.html', ctx)


def get_customer_reviews_page(request):
    ctx = {'title': 'Отзывы',
           'shop_name': SHOP_NAME
           }
    return render(request, 'customer_reviews.html', ctx)