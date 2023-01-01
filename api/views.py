from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from users.models import Post
from .serializers import PostSerializers

class ApiPostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class DetailPost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers