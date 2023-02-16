from django import forms
from django.core.exceptions import ValidationError

from.models import Blog


class BlogCreationForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'theme',]


    def __init__(self, *args, **kwargs):
        super(BlogCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) > 128:
            raise ValidationError('Lenght too much.')
        elif not title.istitle():
            raise ValidationError('Title startswith lowercase.')
        
        return title