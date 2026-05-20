from django.shortcuts import render
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer

from rest_framework import generics

# Create your views here.
class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
