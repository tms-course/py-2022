from django import forms
from django.core.exceptions import ValidationError

from.models import CustomerReview


class CustomerReviewCreationForm(forms.ModelForm):
    class Meta:
        model = CustomerReview
        fields = ['customer_review',]


    def __init__(self, *args, **kwargs):
        super(CustomerReviewCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    

    def clean_customer_review(self):
        customer_review = self.cleaned_data.get('customer_review')

        if len(customer_review) < 30:
            raise ValidationError('Нельзя отправить пустой отзыв.')
        
        return customer_review