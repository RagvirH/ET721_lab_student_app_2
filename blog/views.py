from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

def blog_list(request):
    posts = BlogPost