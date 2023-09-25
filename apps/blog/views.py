from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404, HttpRequest
from django.shortcuts import render

from apps.blog.models import Page, Post


def index(request: HttpRequest, slug=''):
    posts = Post.objects.get_published()
    page_title = 'Home'

    if slug:
        if '/tag/' in request.path_info:
            posts = posts.filter(tags__slug=slug)
            posts[0].save()
            page_title = (posts[0]
                          .tags
                          .filter(slug=slug)
                          .first()
                          .name)

        if '/category/' in request.path_info:
            posts = posts.filter(category__slug=slug)
            page_title = posts[0].category.name

    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    return render(request, 'pages/index.html', {
        'posts': page_posts,
        'page_title': page_title
    })


def post(request, slug):
    post_obj = (Post.objects
                .get_published()
                .filter(slug=slug)
                .first())

    if post_obj is None:
        raise Http404()

    return render(request, 'pages/post.html', {
        'post': post_obj,
        'page_title': post_obj.title
    })


def page(request, slug):
    page_obj = (Page.objects
                .get_published()
                .filter(slug=slug)
                .first())

    if page_obj is None:
        raise Http404()

    return render(request, 'pages/page.html', {
        'page': page_obj,
        'page_title': page_obj.title
    })


def search(request):
    search_value = request.GET.get('q', '').strip()

    search_filter = (
        Q(title__icontains=search_value) |
        Q(excerpt__icontains=search_value) |
        Q(content__icontains=search_value)
    )

    posts = (Post.objects
             .get_published()
             .filter(search_filter))

    return render(request, 'pages/index.html', {
        'posts': posts,
        'search_value': search_value,
        'page_title': search_value
    })
