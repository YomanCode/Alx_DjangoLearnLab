from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from .models import Book

@permission_required('app_name.can_view', raise_exception=True)  # Replace 'app_name' with your app's name
def book_list(request):
    """
    View to display a list of all books, restricted by permission.
    """
    try:
        books = Book.objects.all()  # Fetch all books
        return render(request, 'books/book_list.html', {'books': books})
    except PermissionDenied:
        return render(request, '403.html', status=403)  # Render a custom "403 Forbidden" page
