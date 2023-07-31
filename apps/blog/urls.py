from django.urls import path

from apps.blog.views import index

app_name = 'blog'

urlpatterns = [
    path('', index, name='index')
]
