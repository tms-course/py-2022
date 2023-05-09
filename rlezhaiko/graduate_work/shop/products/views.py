from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages

from categories.models import Category
from .models import Product, ProductReview
from .forms import ProductReviewCreationForm
from settings.base import SHOP_NAME


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
    reviews = ProductReview.objects.filter(status=ProductReview.STATUS_PUBLISHED)

    if request.method == 'POST':
       form = ProductReviewCreationForm(request.POST)
        
       if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.product = product
            review.save()
            url = reverse('product_details_slug', args=(product.slug,))
            messages.success(request, "Ваш отзыв отправлен." )

            return redirect(url)
    else:
        form = ProductReviewCreationForm()
        category_all = Category.objects.all()
        product = get_object_or_404(Product, slug=product_slug)

    ctx = {
        'title': product.name,
        'shop_name': SHOP_NAME,
        'categories': list(category_all),
        'product': product,
        'form': form,
        'reviews': list(reviews),
    }

    return render(request, 'product_details.html', ctx)