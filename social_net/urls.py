# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('posts.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
