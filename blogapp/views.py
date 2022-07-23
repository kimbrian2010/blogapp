from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'blogapp/index.html')

@login_required()
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogapp/home.html', context)


def user_profile_post(request):
    context = {
        'posts': Post.objects.filter(author=request.user)
    }
    return render(request, 'blogapp/user_post.html', context)


def about(request):
    return render(request, 'blogapp/about.html')
