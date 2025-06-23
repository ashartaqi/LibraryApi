from library.models import Author, Book
from library.serializers import AuthorSerializer, BookSerializer
from rest_framework import viewsets ,permissions, status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response


class AuthorSignUp(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]


class AuthorSearch(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        author = self.get_queryset().filter(username=pk).first()
        if author:
            serialzer = self.get_serializer(author)
            serialzer.data
            return Response(serialzer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
  
  
