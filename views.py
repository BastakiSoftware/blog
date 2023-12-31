from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.published.all()


class PostDetailView(DetailView):
    model = Post
