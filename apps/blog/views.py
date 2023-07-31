from django.shortcuts import render


def index(request):
    print('hello')
    return render(request, 'blog/index.html')
