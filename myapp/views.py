from gc import get_objects

from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Comment

# Create your views here.
def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post_details(request):
   post =get_object_or_404(BlogPost, pk=1)
   comments = post.objects.all()
   return render(request, 'post_details.html', {'post': post, 'comments': comments})