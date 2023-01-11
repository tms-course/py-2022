import datetime as dt

from django.shortcuts import render

from .models import Event

def list_events(request):
    events = Event.objects.filter(datetime__gte=dt.datetime.now())
    ctx = {
        'title': 'Events list',
        'events': list(events),
    }
    return render(request, 'event_list.html', ctx)
