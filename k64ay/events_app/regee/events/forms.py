from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Event


class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organizer', 'attendees', 'slug', ]

    def __init__(self, *args, **kwargs):
        super(EventCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name) > 20:
            raise ValidationError(_('Name is too long, make it shorter'))

        return name
    
    def clean_location(self):
        location = self.cleaned_data.get('location')

        if location != 'Minsk':
            raise ValidationError(_('Works only for Minsk'))
        
        return location