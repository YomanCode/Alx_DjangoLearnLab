from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        """
        Create sample data for testing:
        - Two authors
        - Three books with different titles, publication years, and authors
        """
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author=self.author1)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2021, author=self.author1)
        self.book3 = Book.objects.create(title="Book Three", publication_year=2019, author=self.author2)
        self.list_url = reverse('book-list')
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})

    def test_get_all_books(self):
        """Test retrieving all books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # Ensure 3 books are returned

    def test_get_single_book(self):
        """Test retrieving a single book by ID"""
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book(self):
        """Test creating a new book"""
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author1.id,
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)  # Ensure the book count increased
        self.assertEqual(Book.objects.last().title, 'New Book')

    def test_update_book(self):
        """Test updating an existing book"""
        data = {
            'title': 'Updated Book',
            'publication_year': 2022,
            'author': self.author2.id,
        }
        response = self.client.put(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')
        self.assertEqual(self.book1.author, self.author2)

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)  # Ensure the book count decreased

    def test_filter_books_by_author(self):
        """Test filtering books by author"""
        response = self.client.get(self.list_url, {'author__name': self.author1.name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Only books by author1 should be returned

    def test_search_books_by_title(self):
        """Test searching for books by title"""
        response = self.client.get(self.list_url, {'search': 'Book Two'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only Book Two should be returned

    def test_order_books_by_year(self):
        """Test ordering books by publication year"""
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))  # Ensure books are ordered by publication year
