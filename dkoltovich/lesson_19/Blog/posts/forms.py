from django import forms
from .models import Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['created_time', 'edited_time', 'blog', 'status']

    def __init__(self, *args, **kwargs):
        super(PostCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class PostSearchingForm(forms.Form):
    post_title = forms.CharField(max_length=64, label='Post title')
