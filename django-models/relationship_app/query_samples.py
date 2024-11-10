# relationship_app/query_samples.py

import django
import os

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author using .filter()
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # Using .filter() method
        print(f"Books by {author.name} (using .filter()):")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'.")

# 2. List all books in a specific library
def query_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Using related_name 'books'
        print(f"Books in the library '{library.name}':")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")

# 3. Retrieve the librarian for a specific library
def query_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"The librarian for '{library.name}' is {librarian.name}.")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for the library '{library.name}'.")

# Sample Data Insertion (Optional)
def create_sample_data():
    author1 = Author.objects.create(name="Yoman Asfaw")
    author2 = Author.objects.create(name="Jane Doe")

    book1 = Book.objects.create(title="Django for Beginners", author=author1)
    book2 = Book.objects.create(title="Advanced Django", author=author1)
    book3 = Book.objects.create(title="Python Mastery", author=author2)

    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="Community Library")

    library1.books.add(book1, book2)
    library2.books.add(book2, book3)

    Librarian.objects.create(name="John Smith", library=library1)
    Librarian.objects.create(name="Alice Johnson", library=library2)

    print("Sample data created successfully!")

# Run sample queries
if __name__ == "__main__":
    create_sample_data()
    query_books_by_author("Yoman Asfaw")
    query_books_in_library("Central Library")
    query_librarian_for_library("Central Library")
