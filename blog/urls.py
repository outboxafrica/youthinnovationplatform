from django.conf.urls import url, include
from django.contrib import admin
from . import views
from blog.views import PostList

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post_list'),
    # url(r'^$', views.post_list, name='post_list'),
    url(r'(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
]
