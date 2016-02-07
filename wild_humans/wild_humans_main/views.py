from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    context = RequestContext(request)

    context_dict = {}

    return render_to_response('wild_humans_main/index.html', context_dict, context)
