from django import forms
from .models import Blog


class BlogCreationForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['creation_date', 'author']

    def __init__(self, *args, **kwargs):
        super(BlogCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
