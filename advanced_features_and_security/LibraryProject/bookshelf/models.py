# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    author = models.CharField(max_length=100)  # Author name
    published_date = models.DateField()  # Date of publication
    isbn = models.CharField(max_length=13, unique=True)  # ISBN number
    summary = models.TextField(blank=True, null=True)  # Optional summary of the book
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated on save

    class Meta:
        permissions = [
            ("can_view", "Can view books"),
            ("can_create", "Can create books"),
            ("can_edit", "Can edit books"),
            ("can_delete", "Can delete books"),
        ]

    def __str__(self):
        return self.title  # String representation of the model