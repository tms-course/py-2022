from django import forms

from.models import Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content',]


    def __init__(self, *args, **kwargs):
        super(PostCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'