from django.shortcuts import render
from models import Event

def index(request):
    events = Event.objects.all().exclude(passed=True)
    passed_events = Event.objects.all().exclude(passed=False)
    context_dict = {'events': events, 'passed_events': passed_events}

    return render(request, 'calendar.html', context_dict)