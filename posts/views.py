# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from posts.models import Post, Like
from posts.serializers import PostSerializer, LikeSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AddLike(generics.CreateAPIView, mixins.DestroyModelMixin):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
