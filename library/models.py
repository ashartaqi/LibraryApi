from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False, default=None)
    biography = models.TextField(max_length=500, blank=True, default='')

    class Meta:
        ordering = ['name']


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, default=None)
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now=True)
    is_borrowed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['title']