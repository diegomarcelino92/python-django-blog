from django.shortcuts import render

from apps.blog.models import Post


def index(request):
    print('hello')
    posts = Post.objects.all()
    return render(request, 'pages/index.html', {'posts': posts})
