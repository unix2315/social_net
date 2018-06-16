# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User,
                               related_name='posts',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(
        auto_now_add=True, null=True
    )

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User,
                             related_name='likes',
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             related_name='likes',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True, null=True
    )
