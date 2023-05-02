from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_page

from .models import CustomerReview
from .forms import CustomerReviewCreationForm
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
           'products': list(products),
           }

    return render(request, 'home_page.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_about_us_page(request):
    category = Category.objects.all()
    count = Product.objects.count()
    ctx = {'title': 'О нас',
           'categories': list(category),
           'count': count,
           'shop_name': SHOP_NAME,
           }
    return render(request, 'about_us.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_transport_services_page(request):
    category = Category.objects.all()
    ctx = {'title': 'Транспортные услуги',
           'categories': list(category),
           'shop_name': SHOP_NAME,
           }
    return render(request, 'transport_services.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_mission_and_values_page(request):
    category = Category.objects.all()
    ctx = {'title': 'Миссия и ценности',
           'categories': list(category),
           'shop_name': SHOP_NAME,
           }
    return render(request, 'mission_and_values.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_delivery_page(request):
    category = Category.objects.all()
    ctx = {'title': 'Доставка',
           'categories': list(category),
           'shop_name': SHOP_NAME,
           }
    return render(request, 'delivery.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_equipment_repair_page(request):
    category = Category.objects.all()
    ctx = {'title': 'Ремонт техники',
           'categories': list(category),
           'shop_name': SHOP_NAME,
           }
    return render(request, 'equipment_repair.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_replacement_and_return_products(request):
    category = Category.objects.all()
    ctx = {'title': 'Замена и возврат товара',
           'categories': list(category),
           'shop_name': SHOP_NAME,
           }
    return render(request, 'replacement_and_return_products.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_payment_page(request):
    category = Category.objects.all()
    ctx = {'title': 'Оплата',
           'categories': list(category),
           'shop_name': SHOP_NAME,
           }
    return render(request, 'payment.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def get_contacts_page(request):
    category = Category.objects.all()
    ctx = {'title': 'Контакты',
           'categories': list(category),
           'shop_name': SHOP_NAME,
           }
    return render(request, 'contacts.html', ctx)


@cache_page(60 * 20)
def get_customer_reviews_page(request):
    category = Category.objects.all()
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
           'categories': list(category),
           'shop_name': SHOP_NAME,
           'reviews': reviews,
           }
    
    return render(request, 'customer_reviews.html', ctx)


@cache_page(60 * 60 * 24 * 10)
def create_review(request):
    category = Category.objects.all()
    if request.method == 'POST':
       form = CustomerReviewCreationForm(request.POST)
        
       if form.is_valid():
           review = form.save(commit=False)
           review.author = request.user
           review.save()
           
           return redirect('customer_reviews_page')
    else:
       form = CustomerReviewCreationForm()
    
    ctx = {
          'form': form,
          'categories': list(category),
        }

    return render(request, 'review_create.html', ctx)