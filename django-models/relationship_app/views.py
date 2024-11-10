# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Library  # Importing Library model

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library  # Specifies the model to use
    template_name = 'relationship_app/library_detail.html'  # Specifies the template
    context_object_name = 'library'  # Sets the context variable for the template
