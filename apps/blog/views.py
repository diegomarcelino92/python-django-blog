from django.core.paginator import Paginator
from django.shortcuts import render

from apps.blog.models import Post


def index(request):
    posts = Post.objects.get_published()

    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    return render(request, 'pages/index.html', {'posts': page_posts})


def post(request):
    return render(request, 'pages/post.html')


def page(request):
    return render(request, 'pages/page.html')
