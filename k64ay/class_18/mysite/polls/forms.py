from django import forms


class QuestionForm(forms.Form):
    question_text = forms.CharField(
        max_length=256, 
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    pub_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }, format='%d/%m/%Y %H:%M')
    )