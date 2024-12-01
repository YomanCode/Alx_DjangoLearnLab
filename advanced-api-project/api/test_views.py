from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        """
        Set up test data:
        - Create authors and books
        - Set up a test user and token for authentication
        """
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author=self.author1)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2021, author=self.author1)
        self.book3 = Book.objects.create(title="Book Three", publication_year=2019, author=self.author2)

        self.user = User.objects.create_user(username="testuser", password="password")
        self.token = Token.objects.create(user=self.user)
        self.auth_headers = {"HTTP_AUTHORIZATION": f"Token {self.token.key}"}

        self.list_url = reverse('book-list')
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})

    def test_unauthenticated_access(self):
        """Test that unauthenticated users can only view books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        create_response = self.client.post(self.list_url, {
            'title': 'Unauthorized Book',
            'publication_year': 2023,
            'author': self.author1.id,
        })
        self.assertEqual(create_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_access(self):
        """Test that authenticated users can perform CRUD operations"""
        # Test creating a book
        create_response = self.client.post(self.list_url, {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author1.id,
        }, **self.auth_headers)
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        # Test updating a book
        update_response = self.client.put(self.detail_url(self.book1.id), {
            'title': 'Updated Book',
            'publication_year': 2022,
            'author': self.author2.id,
        }, **self.auth_headers)
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

        # Test deleting a book
        delete_response = self.client.delete(self.detail_url(self.book1.id), **self.auth_headers)
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books_by_author(self):
        """Test filtering books by author"""
        response = self.client.get(self.list_url, {'author__name': self.author1.name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_books_by_title(self):
        """Test searching for books by title"""
        response = self.client.get(self.list_url, {'search': 'Book Two'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        """Test ordering books by publication year"""
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
