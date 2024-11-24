from django.shortcuts import render
from .forms import ExampleForm  # Import the ExampleForm
from .models import Book

def search_books(request):
    form = ExampleForm(request.GET or None)  # Initialize the form with GET data if available
    books = []

    # If the form is valid, perform the search
    if form.is_valid():
        query = form.cleaned_data['query']  # Get the search query from the form
        books = Book.objects.filter(title__icontains=query)  # Search books by title

    return render(request, 'bookshelf/form_example.html', {'form': form, 'books': books})
