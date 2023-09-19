from django.shortcuts import render
from .models import *

# Create your views here.
def home_view(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_posts/home.html', {'posts': posts})

def new_post_view(request):
    return render(request, 'blog_posts/new_post.html')