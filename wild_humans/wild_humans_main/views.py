from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Blog
from event_calendar.models import Event
from cover_page.models import CoverImage


def index(request):
    context = RequestContext(request)

 #   last_three_posts = Blog.objects.latest()
    latest_blog = Blog.objects.latest('publish_date')
    events = Event.objects.all().exclude(passed=True)
    passed_events = Event.objects.all().exclude(passed=False)
    cover_images = CoverImage.objects.all()
    print cover_images
    print len(cover_images)
    if len(cover_images) < 3:
        num_images = range(1, 2)
    else:
        num_images = range(1, len(cover_images) - 1)
    print 'num images {}'.format(num_images)

    context_dict = {'latest_blog': latest_blog, 'passed_events': passed_events, 'cover_images': cover_images, 'num_images': num_images, 'events': events}

    return render_to_response('wild_humans_main/index.html', context_dict, context)


def listen(request):
    context = RequestContext(request)

    return render_to_response('wild_humans_main/listen.html', {}, context)