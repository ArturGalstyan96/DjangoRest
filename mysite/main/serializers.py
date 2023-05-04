from .models import Book, Author
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'about', 'author', 'creation_date')



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('fname', 'lname', 'birth_date')