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

# Security Settings for HTTPS and Secure Cookies

# Redirect all HTTP traffic to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS) settings
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow preloading to ensure HTTPS connection

# Secure cookies (only transmitted over HTTPS)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Security headers to mitigate clickjacking, MIME sniffing, and XSS attacks
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
