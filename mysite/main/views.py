from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_params = ["name", "about", "author", "creation_date"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_kwargs = dict()
        for param in self.filter_params:
            value = self.request.query_params.get(param)
            if value is not None:
                filter_kwargs[param] = value
        queryset = queryset.filter(**filter_kwargs)
        return queryset

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.update()
        return Response(status=status.HTTP_204_NO_CONTENT)