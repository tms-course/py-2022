import datetime as dt

from django.test import TestCase
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

from events.models import Event


class TestModels(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.user = User.objects.get(username='admin')
        self.event1 = Event.objects.create(
            organizer=self.user,
            name='Event 1',
            datetime=dt.datetime.now(),
            location='Minsk',
            # slug='event-1'
        )

    def test_event_is_assigned_slug_on_creation(self):
        self.assertEquals(self.event1.slug, 'event-1')

    def test_unique_event_slug(self):
        with self.assertRaises(IntegrityError):
            Event.objects.create(
                organizer=self.user,
                name='Event 1',
                datetime=dt.datetime.now(),
                location='Minsk',
                # slug='event-1'
            )
