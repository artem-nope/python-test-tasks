from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    # author = serializers.SlugRelatedField(slug_field='last', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'cover']


class BookSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'cover']


class AuthorSerializer(serializers.ModelSerializer):
    # books = serializers.StringRelatedField(many=True)
    books = BookSerializer1(many=True)

    class Meta:
        model = Author
        fields = ['id', 'first', 'last', 'portrait', 'books']


