from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, help_text="The author's name")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, help_text="The title of the book")
    publication_year = models.PositiveIntegerField(help_text="The year the book was published")
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books',
        help_text="The author of the book"
    )

    def __str__(self):
        return self.title

# The Author model represents authors with a name.
# Each Author can have multiple associated Book instances.

# The Book model represents books with a title, publication year, and a foreign key to an Author.