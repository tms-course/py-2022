from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')