import datetime as dt

from django.test import SimpleTestCase

from events.forms import EventCreationForm


class TestForms(SimpleTestCase):

    def test_location_is_minsk_only(self):
        form = EventCreationForm(data={
            'name': 'Event 1',
            'datetime': dt.datetime.now(),
            'location': 'Minsk',
        })

        self.assertTrue(form.is_valid())

    def test_invalid_location(self):
        form = EventCreationForm(data={
            'name': 'Event 1',
            'datetime': dt.datetime.now(),
            'location': 'Gdansk',
        })

        self.assertFalse(form.is_valid())


    def test_event_name_should_be_trimmed(self):
        form = EventCreationForm(data={
            'name': '  Event 1  ',
            'datetime': dt.datetime.now(),
            'location': 'Minsk',
        })

        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data['name'], 'Event 1')


    def test_name_length(self):
        form = EventCreationForm(data={
            'name': '123456789123456789123456789',
            'datetime': dt.datetime.now(),
            'location': 'Minsk',
        })

        self.assertFalse(form.is_valid())