import datetime as dt

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseNotFound

from .forms import EventCreationForm
from .models import Event

def list_events(request):
    events = Event.objects.filter(datetime__gte=dt.datetime.now())
    ctx = {
        'title': 'Events list',
        'events': list(events),
    }
    return render(request, 'event_list.html', ctx)

def create_event(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST, request.FILES)
        
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
    else:
        form = EventCreationForm()
    
    ctx = {'form': form}

    return render(request, 'event_create.html', ctx)

def get_event(request, event_id: int):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return HttpResponseNotFound('Event does not exists')

    ctx = {
        'event': event, 
        'attendees': list(event.attendees.all()),
        'has_user_joint': event.attendees\
            .filter(pk=request.user.id)\
            .exists()
    }

    return render(request, 'event_details.html', ctx)

def delete_event(request, event_id: int):
    Event.objects.filter(id=event_id).delete()

    return redirect('event_list')

def join_event(request, event_id: int):
    if request.method == 'POST':
        event = get_object_or_404(Event, pk=event_id)
        event.attendees.add(request.user)

    return redirect('event_details', event_id=event_id)