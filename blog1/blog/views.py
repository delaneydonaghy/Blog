from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Topic
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "topic", "body", "image"]

    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "topic", "body", "image"]  

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home") 

class TopicListView(ListView):
    model = Topic
    template_name = "topic.html"
