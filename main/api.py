__author__ = 'night'
# coding=utf-8
from django.views.decorators.csrf import csrf_exempt

__author__ = 'night'

from django.http import HttpResponse

from main import db
from serializers import BookSerializers
from rest_framework.renderers import JSONRenderer


@csrf_exempt
def get_books(request):
    if request.method == 'POST':
        book_id = request.GET.get("id", "")
        book = db.get_book(book_id)
        return HttpResponse(JSONRenderer().render(BookSerializers(book).data))
    else:
        book_id = request.GET.get("id", "")
        book = db.get_book(book_id)
        return HttpResponse(JSONRenderer().render(BookSerializers(book).data))