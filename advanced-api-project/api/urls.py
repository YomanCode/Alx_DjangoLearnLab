from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/add/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]

# BookListView:
# - Provides a read-only view to list all books.
# - Accessible to both authenticated and unauthenticated users.

# BookDetailView:
# - Retrieves details of a single book by ID.
# - Accessible to both authenticated and unauthenticated users.

# BookCreateView:
# - Allows authenticated users to add new books.
# - Includes custom validation for publication year.

# BookUpdateView:
# - Allows authenticated users to update existing books.
# - Includes custom validation for publication year.

# BookDeleteView:
# - Allows authenticated users to delete books.
