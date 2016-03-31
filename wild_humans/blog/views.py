from django.shortcuts import render_to_response, get_object_or_404, render
from .models import Blog

# Create your views here
#
def index(request):
    posts = Blog.objects.all()
    context_dict = {'posts': posts}
    print(posts)
    print(posts[0])
    print(posts[0].title)
    return render(request, 'blog.html', context_dict)

def post(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    context_dict = {'post': post}

    return render(request, 'post.html', context_dict)