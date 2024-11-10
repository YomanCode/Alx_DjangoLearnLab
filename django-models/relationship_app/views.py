# relationship_app/views.py

from django.shortcuts import render
from .models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    # Explicitly specify the template path "relationship_app/list_books.html"
    return render(request, 'relationship_app/list_books.html', {'books': books})

