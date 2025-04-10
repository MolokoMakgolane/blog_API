from django.shortcuts import render
from rest_framework import generics
from blog_API import serializers
from django.contrib.auth.models import User

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class PostList(generics.ListCreateAPIView):
    queryset = 'Post'.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = 'Post'.objects.all()
    serializer_class = serializers.PostSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = 'Comment'.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = ['permissions'.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = 'Comment'.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = ['permissions'.IsAuthenticatedOrReadOnly,
                          'IsauthorOrReadOnly']   
