from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'username': 'User1',
        'name': 'Name of Poster',
        'title': 'Title 1',
    },
    {
        'username': 'User2',
        'name': 'Name of Poster',
        'title': 'Title 2',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home/base.html', context)
