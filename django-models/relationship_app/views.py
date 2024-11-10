# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library  # Specifies the model to use
    template_name = 'relationship_app/library_detail.html'  # Template for the view
    context_object_name = 'library'  # Sets the context variable name for the template
