from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import date
from .serializers import BookSerializer

# ListView: Retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Add filtering, searching, and ordering backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Specify fields available for filtering
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Specify fields available for search
    search_fields = ['title', 'author__name']

    # Specify fields available for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Custom validation: ensure publication year is not in the future
        publication_year = serializer.validated_data.get('publication_year')
        if publication_year > date.today().year:
            raise ValueError("Publication year cannot be in the future.")
        serializer.save()

# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # Custom validation: ensure publication year is not in the future
        publication_year = serializer.validated_data.get('publication_year')
        if publication_year > date.today().year:
            raise ValueError("Publication year cannot be in the future.")
        serializer.save()

# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


### Filtering
Filter books by title, author name, or publication year:
- /books/?title=SomeTitle
- /books/?author__name=SomeAuthor
- /books/?publication_year=2023

### Searching
Search books by keywords in the title or author name:
- /books/?search=Keyword

### Ordering
Order books by title or publication year (ascending or descending):
- /books/?ordering=title
- /books/?ordering=-publication_year
