from django.test import SimpleTestCase
from django.urls import reverse, resolve

from products.views import *


class TestUrls(SimpleTestCase):   
    def test_list_product_resolves(self):
        url = reverse('product_list')
        self.assertEquals(resolve(url).func, list_product)
    

    def test_get_product_by_slug_resolves(self):
        url = reverse('product_details_slug', args=('kholodilnik-s-morozilnikom-lg-doorcooling-gw-b509clzm',))
        self.assertEquals(resolve(url).func, get_product_by_slug)