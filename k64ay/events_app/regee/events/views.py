import datetime as dt

from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound

from .models import Event

def list_events(request):

    if request.method == 'POST':
        name = request.POST['name']
        datetime = dt.datetime.strptime(
            request.POST['datetime'], '%Y-%m-%d %H:%M:%S')
        location = request.POST['location']

        Event.objects.create(
            name=name,
            datetime=datetime,
            location=location
        )

    events = Event.objects.filter(datetime__gte=dt.datetime.now())
    ctx = {
        'title': 'Events list',
        'events': list(events),
    }
    return render(request, 'event_list.html', ctx)

def create_event(request):
    return render(request, 'event_create.html')

def get_event(request, event_id: int):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return HttpResponseNotFound('Event does not exists')

    ctx = {'event': event}

    return render(request, 'event_details.html', ctx)