from django.urls import path

from apps.blog.views import author, index, page, post, search

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/<slug:slug>/', post, name='post'),
    path('page/<slug:slug>/', page, name='page'),
    path('tag/<slug:slug>/', index, name='tag'),
    path('category/<slug:slug>/', index, name='category'),
    path('author/<int:author_id>/', author, name='author'),
    path('search/', search, name='search'),
]
