from django.test import SimpleTestCase
from django.urls import resolve, reverse

from events.views import list_events, create_event, get_event_by_slug


class TestUrls(SimpleTestCase):
    
    def test_list_events_url_resolves(self):
        url = reverse('event_list')
        print(url)
        self.assertEquals(resolve(url).func, list_events)

    def test_create_event_url_resolves(self):
        url = reverse('create_event')
        print(url)
        self.assertEquals(resolve(url).func, create_event)

    def test_event_details_slug_url_resolves(self):
        url = reverse('event_details_slug', args=('hello-world',))
        self.assertEquals(resolve(url).func, get_event_by_slug)