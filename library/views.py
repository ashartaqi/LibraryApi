from library.models import Author, Book
from library.serializers import AuthorSerializer, BookSerializer
from rest_framework import permissions

from rest_framework import viewsets


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
  
  
