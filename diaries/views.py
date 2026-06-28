from django.shortcuts import render
from django.views import generic
from .models import Post
# from django.http import HttpResponse

# Create your views here.
# def my_diaries(request):
#     return HttpResponse("Hello, blog!")
class PostList(generic.ListView):
    model = Post
