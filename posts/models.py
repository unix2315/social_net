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

    @property
    def like_count(self):
        return self.likes.count()

    def add_like(self, user):
        like, is_created = Like.objects.get_or_create(
            post=self, user=user
        )
        return like

    def remove_like(self, user):
        Like.objects.filter(
            post=self, user=user
        ).delete()


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
