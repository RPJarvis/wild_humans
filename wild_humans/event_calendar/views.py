from django.shortcuts import render
from models import Event

def index(request):
    events = Event.objects.all()
    context_dict = {'events': events}

    return render(request, 'calendar.html', context_dict)