from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Nordo',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'august 27, 2018'
    },
    {
        'author': 'Nord',
        'title': 'Blog Post 2',
        'content': 'Secound post content',
        'date_posted': 'august 9, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})