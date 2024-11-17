# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books and their authors
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # The model to retrieve data from
    template_name = 'relationship_app/library_detail.html'  # Template for displaying library details
    context_object_name = 'library'  # The context name that will hold the library data in the template
