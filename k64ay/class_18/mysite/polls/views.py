import datetime as dt

from django.shortcuts import render
from django.http import HttpResponse

from .forms import QuestionForm
from .models import Question

def index(request):
    if request.method == 'POST':
        postForm = QuestionForm(request.POST, request.FILES)
        if postForm.is_valid():
            postForm.save()
            
    date = dt.datetime.now()
    questionForm = QuestionForm()
    
    return render(request, 'index.html', {
        'now': date,
        'form': questionForm,
    })
