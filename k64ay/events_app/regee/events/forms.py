from django import forms

from .models import Event


class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organizer', 'attendees',]

    def __init__(self, *args, **kwargs):
        super(EventCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
