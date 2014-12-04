__author__ = 'night'
# coding=utf-8

from django.http import HttpResponse

from main import db
from serializers import BookSerializers
from rest_framework.renderers import JSONRenderer


def get_books(request):
    if request.method == 'POST':
        book_ids = request.POST.get("ids", "")
        books = db.get_books(book_ids)
        return HttpResponse(JSONRenderer().render(BookSerializers(books, many=True).data))
    else:
        book_ids = request.GET.get("ids", "")
        books = db.get_books(book_ids)
        return HttpResponse(JSONRenderer().render(BookSerializers(books, many=True).data))