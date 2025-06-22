from rest_framework import serializers
from library.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='book_set')
    class Meta:
        model = Author
        fields = ['id','first_name','last_name', 'username', 'email','password', 'biography', 'books']
    
    def create(self, request):
        password = request.pop('password')
        user = Author(**request)
        user.set_password(password)
        user.save()
        return user


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date', 'is_borrowed']