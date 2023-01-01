from django.shortcuts import render
from .models import Post
# Create your views here.
from django.views.generic.edit import CreateView
class PostDetailView(CreateView):
    template_name = 'forms.html'
    fields = '__all__'
    model = Post