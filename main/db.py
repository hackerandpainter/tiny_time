__author__ = 'night'
from models import Book


def get_books(book_ids):
    # todo add get book logic
    # book = Book.objects.get(id=book_ids)
    books = Book.objects.all()
    return books