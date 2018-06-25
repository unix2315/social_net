# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from posts import views


urlpatterns = [
    url(r'^posts/$', views.PostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/like$', views.AddLike.as_view()),
]
