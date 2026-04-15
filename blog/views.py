

from django.shortcuts import render

def home(request):
    context = {
        'name': 'Hassan',
        'posts': ['My first post', 'My second post', 'My third post'],
    }
    return render(request, 'blog/home.html', context)