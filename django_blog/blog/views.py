from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# View to list all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# View to show the details of a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# View to create a new post
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']  # Fields for the form
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')  # Redirect to the post list after creation

# View to update an existing post
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']  # Fields for the form
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')  # Redirect to the post list after update

# View to delete a post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')  # Redirect to the post list after deletion
