from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    biography = models.TextField(max_length=500, blank=True, default='')


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, default=None)
    description = models.CharField(max_length=500, blank=False, default=None)
    content = models.CharField(max_length=500, blank=True, default="this book is empty")
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now=True)
    is_borrowed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['title']