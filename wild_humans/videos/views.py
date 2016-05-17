from django.shortcuts import render
from models import Video

# Create your views here.
def index(request):
    videos = Video.objects.all()
    context_dict = {'videos': videos}

    return render(request, 'videos.html', context_dict)