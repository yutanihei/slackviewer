from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Channel, User

# Create your views here.

def home(request):
    posts = Post.objects.order_by("ts")
    channels = Channel.objects.order_by("name")
    return render(request, 'viewer/home.html', {'posts': posts, 'channels': channels})

def post_list(request, name):
    posts = Post.objects.filter(channel__name=name).order_by("ts")
    channels = Channel.objects.order_by("name")
    return render(request, 'viewer/home.html', {'posts': posts, 'channels': channels})