from rest_framework import serializers
from library.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='book_set')
    class Meta:
        model = Author
        fields = ['id' ,'first_name' ,'last_name' ,'username', 'email', 'password', 'biography' ,'books']

        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = Author(**validated_data)
        user.set_password(password)
        user.save()
        print(user)
        return user


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date', 'is_borrowed']