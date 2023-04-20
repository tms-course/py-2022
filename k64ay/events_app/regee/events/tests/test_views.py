import datetime as dt

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from events.models import Event


class TestViews(TestCase):

    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.get(username='admin')

    def test_event_list_GET(self):
        response = self.client.get(reverse('event_list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'event_list.html')

    def test_event_details_slug_GET(self):
        Event.objects.create(
            organizer=self.user,
            name='Event 1',
            datetime=dt.datetime.now(),
            location='Minsk',
        )
        response = self.client.get(reverse('event_details_slug', args=('event-1',)))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'event_details.html')


    def test_event_create_POST(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('create_event'), {
            'name': 'Event 2',
            'datetime': dt.datetime.now(),
            'location': 'Minsk',
        })

        self.assertEquals(response.status_code, 302)

    def test_event_delete_POST(self):
        event1 = Event.objects.create(
            organizer=self.user,
            name='Event 3',
            datetime=dt.datetime.now(),
            location='Minsk',
        )
        response = self.client.post(reverse('event_delete', args=(event1.id,)))
        
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Event.objects.count(), 0)