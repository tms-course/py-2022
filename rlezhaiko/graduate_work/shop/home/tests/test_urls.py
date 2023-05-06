from django.test import SimpleTestCase
from django.urls import reverse, resolve

from home.views import *


class TestUrls(SimpleTestCase):   
    def test_get_home_page_resolves(self):
        url = reverse('home_page')
        self.assertEquals(resolve(url).func, get_home_page)
    

    def test_get_about_us_page_resolves(self):
        url = reverse('about_us_page')
        self.assertEquals(resolve(url).func, get_about_us_page)


    def test_get_transport_services_page_resolves(self):
        url = reverse('transport_services_page')
        self.assertEquals(resolve(url).func, get_transport_services_page)
    

    def test_get_mission_and_values_page_resolves(self):
        url = reverse('mission_and_values_page')
        self.assertEquals(resolve(url).func, get_mission_and_values_page)
    

    def test_get_delivery_page_resolves(self):
        url = reverse('delivery_page')
        self.assertEquals(resolve(url).func, get_delivery_page)
    

    def test_get_equipment_repair_page_resolves(self):
        url = reverse('equipment_repair_page')
        self.assertEquals(resolve(url).func, get_equipment_repair_page)
    

    def test_get_replacement_and_return_products_resolves(self):
        url = reverse('replacement_and_return_products_page')
        self.assertEquals(resolve(url).func, get_replacement_and_return_products)
    

    def test_get_payment_page_resolves(self):
        url = reverse('payment_page')
        self.assertEquals(resolve(url).func, get_payment_page)
    

    def test_get_contacts_page_resolves(self):
        url = reverse('contacts_page')
        self.assertEquals(resolve(url).func, get_contacts_page)
    

    def test_get_customer_reviews_page_resolves(self):
        url = reverse('customer_reviews_page')
        self.assertEquals(resolve(url).func, get_customer_reviews_page)


    def test_create_review_resolves(self):
        url = reverse('review_create')
        self.assertEquals(resolve(url).func, create_review)