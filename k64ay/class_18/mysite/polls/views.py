import datetime as dt

from django.shortcuts import render
from django.http import HttpResponse

from .forms import QuestionForm
from .models import Question

def index(request):
    date = dt.datetime.now()
    questionForm = QuestionForm()
    
    return render(request, 'index.html', {
        'now': date,
        'form': questionForm,
    })
