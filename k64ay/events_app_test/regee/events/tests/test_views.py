import json
import datetime as dt

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from events.models import Event


class TestView(TestCase):
    fixtures = ['users.json']
    
    def setUp(self):
        self.client = Client()
        self.event_list_url = reverse('event_list')
        self.event_create_url = reverse('create_event')
        self.user = User.objects.get(username='admin')

    def test_event_list_GET(self):
        res = self.client.get(self.event_list_url)

        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed(res, 'event_list.html')


    def test_event_details_slug_GET(self):
        Event.objects.create(
            organizer=self.user,
            name='Event 2',
            datetime=dt.datetime.now(),
            location = 'Minsk',
        )
        res = self.client.get(reverse('event_details_slug', args=['event-2']))

        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed('event_details.html')

    def test_event_create_POST(self):
        self.client.login(username='admin', password='admin')
        res = self.client.post(self.event_create_url, {
            'name': 'Test event',
            'datetime': '2023-04-05 10:00:00',
            'location': 'Minsk',
        })
        self.assertEquals(res.status_code, 302)

    def test_event_delete_POST(self):
        event1 = Event.objects.create(
            organizer=self.user,
            name='Test event 1',
            datetime=dt.datetime.now(),
            location = 'Minsk',
        )
        self.assertEquals(Event.objects.count(), 1)
        res = self.client.post(reverse('event_delete', args=(event1.id,)))
        self.assertEquals(res.status_code, 302)
        
        self.assertEquals(Event.objects.count(), 0)
