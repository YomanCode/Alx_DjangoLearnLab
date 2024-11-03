book = Book.objects.get(title="Nineteen Eighty-Four") #first retrieving the book
book.delete() #deleting the book
from bookshelf.models import Book #importing Book model
book = Book.objects.all() #and trying to retrieve again to check