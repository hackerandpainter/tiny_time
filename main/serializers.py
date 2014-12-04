__author__ = 'night'
from main.models import Book

__author__ = 'night'
from rest_framework import serializers


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'name', 'artistId', 'artist', 'categoryId', 'category', 'vol', 'like', 'share', 'time', 'paintings')