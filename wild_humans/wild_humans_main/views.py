from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Blog
from event_calendar.models import Event

def index(request):
    context = RequestContext(request)

 #   last_three_posts = Blog.objects.latest()
    latest_blog = Blog.objects.latest('publish_date')
    #TODO: only graby next few events
    events = Event.objects.all()

    context_dict = {'latest_blog': latest_blog, 'events': events}

    return render_to_response('wild_humans_main/index.html', context_dict, context)
