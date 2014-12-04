__author__ = 'night'
from models import Book


def get_book(book_id):
    book = Book.objects.get(id=book_id)
    return book