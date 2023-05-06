from django import forms
from django.core.exceptions import ValidationError

from .models import ProductReview


class ProductReviewCreationForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['product_review',]


    def __init__(self, *args, **kwargs):
        super(ProductReviewCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    

    def clean_customer_review(self):
        product_review = self.cleaned_data.get('product_review')

        if len(product_review) < 30:
            raise ValidationError('Нельзя отправить пустой отзыв.')
        
        return product_review