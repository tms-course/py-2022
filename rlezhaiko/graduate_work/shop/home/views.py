from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_page
from django.contrib import messages

from .models import CustomerReview
from .forms import CustomerReviewCreationForm
from cart.forms import CartAddProductForm
from categories.models import Category
from products.models import Product
from settings.base import SHOP_NAME


def get_home_page(request):
    category = Category.objects.all()
    products = Product.objects.all()
    cart_product_form = CartAddProductForm()

    ctx = {'title': 'Главная',
           'shop_name': SHOP_NAME,
           'name_header': 'name header',
           'name_footer': 'name footer',
           'categories': list(category),
           'products': list(products),
           'cart_product_form': cart_product_form,
           }

    return render(request, 'home_page.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_about_us_page(request):
    count = Product.objects.count()
    ctx = {'title': 'О нас',
           'count': count,
           'shop_name': SHOP_NAME,
           }
    return render(request, 'about_us.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_transport_services_page(request):
    ctx = {'title': 'Транспортные услуги',
           'shop_name': SHOP_NAME,
           }
    return render(request, 'transport_services.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_mission_and_values_page(request):
    ctx = {'title': 'Миссия и ценности',
           'shop_name': SHOP_NAME,
           }
    return render(request, 'mission_and_values.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_delivery_page(request):
    ctx = {'title': 'Доставка',
           'shop_name': SHOP_NAME,
           }
    return render(request, 'delivery.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_equipment_repair_page(request):
    ctx = {'title': 'Ремонт техники',
           'shop_name': SHOP_NAME,
           }
    return render(request, 'equipment_repair.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_replacement_and_return_products(request):
    ctx = {'title': 'Замена и возврат товара',
           'shop_name': SHOP_NAME,
           }
    return render(request, 'replacement_and_return_products.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_payment_page(request):
    ctx = {'title': 'Оплата',
           'shop_name': SHOP_NAME,
           }
    return render(request, 'payment.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_contacts_page(request):
    ctx = {'title': 'Контакты',
           'shop_name': SHOP_NAME,
           }
    return render(request, 'contacts.html', ctx)


@cache_page(60 * 5)
def get_customer_reviews_page(request):
    reviews_list = CustomerReview.objects.filter(status=CustomerReview.STATUS_PUBLISHED)
    page = request.GET.get('page', 1)
    paginator = Paginator(reviews_list, 5)

    try:
       reviews = paginator.page(page)
    except PageNotAnInteger:
       reviews = paginator.page(1)
    except EmptyPage:
       reviews = paginator.page(paginator.num_pages)

    ctx = {'title': 'Отзывы',
           'shop_name': SHOP_NAME,
           'reviews': reviews,
           }
    
    messages.success(request, "Ваш отзыв отправлен." )
    
    return render(request, 'customer_reviews.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def create_review(request):
    if request.method == 'POST':
       form = CustomerReviewCreationForm(request.POST)
        
       if form.is_valid():
           review = form.save(commit=False)
           review.author = request.user
           review.save()
           messages.success(request, "Ваш отзыв отправлен." )

           return redirect('customer_reviews_page')
    else:
       form = CustomerReviewCreationForm()
    
    ctx = {
          'form': form,
        }

    return render(request, 'review_create.html', ctx)