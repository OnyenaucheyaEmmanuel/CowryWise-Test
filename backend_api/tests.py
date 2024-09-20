from django.test import TestCase
from .models import Book

class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title="Test Book", author="Test Author", publisher="Wiley", category="Science", available=True)

    def test_book_creation(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.author, "Test Author")
        