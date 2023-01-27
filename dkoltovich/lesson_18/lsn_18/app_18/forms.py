from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['registration_time']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

