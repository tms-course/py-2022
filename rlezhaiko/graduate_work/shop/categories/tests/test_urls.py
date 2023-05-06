from django.test import SimpleTestCase
from django.urls import reverse, resolve

from categories.views import *


class TestUrls(SimpleTestCase):   
    def test_get_category_page_resolves(self):
        url = reverse('category_page')
        self.assertEquals(resolve(url).func, get_category_page)
    

    def test_get_category_by_slug_resolves(self):
        url = reverse('category_details_slug', args=('kholodilniki',))
        self.assertEquals(resolve(url).func, get_category_by_slug)