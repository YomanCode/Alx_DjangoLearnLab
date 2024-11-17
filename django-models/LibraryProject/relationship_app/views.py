from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Library, Author  # Updated imports

def list_books(request):
    """
    Function-based view to display all books
    """
    books = Book.objects.all().select_related('author')
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """
    Class-based view to display library details
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        """
        Optimize query by prefetching related books and their authors
        """
        return Library.objects.prefetch_related(
            'books', 
            'books__author'
        )