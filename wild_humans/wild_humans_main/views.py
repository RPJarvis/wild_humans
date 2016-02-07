from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    context = RequestContext(request)

    context_dict = {}

    return render_to_response('', context_dict, context)
