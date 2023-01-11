import datetime as dt

from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

def index(request):
    date = dt.datetime.now()
    return render(request, 'index.html', {
        'now': date
    })
