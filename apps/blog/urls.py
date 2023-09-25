from django.urls import path

from apps.blog.views import index, page, post, search

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/<slug:slug>/', post, name='post'),
    path('page/<slug:slug>/', page, name='page'),
    path('category/<slug:slug>/', index, name='category'),
    path('tag/<slug:slug>/', index, name='tag'),
    path('search/', search, name='search'),
]
