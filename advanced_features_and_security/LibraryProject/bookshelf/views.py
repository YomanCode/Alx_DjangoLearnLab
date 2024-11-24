from django.shortcuts import render
from .models import Book

def book_list(request):
    """
    View to display a list of all books.
    """
    books = Book.objects.all()  # Fetch all book records from the database
    return render(request, 'books/book_list.html', {'books': books})