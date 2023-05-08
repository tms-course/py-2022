from django.test import SimpleTestCase
from django.urls import reverse, resolve

from orders.views import *


class TestUrls(SimpleTestCase):   
    def test_create_order_resolves(self):
        url = reverse('order_create')
        self.assertEquals(resolve(url).func, create_order)