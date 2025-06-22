from django.views import View  # Base class-based view

from django.views.generic import TemplateView  # Renders a template
from django.views.generic import ListView  # List objects
from django.views.generic import DetailView  # Detail view of one object
from django.views.generic import CreateView  # Form for creating object
from django.views.generic import UpdateView  # Form for updating object
from django.views.generic import DeleteView  # Confirm + delete
from django.views.generic import RedirectView  # Redirect to URL

from django.views.generic.edit import FormView  # Generic form handler

from rest_framework.views import APIView  # Base class-based API view

from rest_framework.generics import GenericAPIView  # Adds queryset, serializer_class, etc.

from rest_framework.generics import ListAPIView  # Read-only list
from rest_framework.generics import RetrieveAPIView  # Read-only detail
from rest_framework.generics import CreateAPIView  # Create
from rest_framework.generics import UpdateAPIView  # Update
from rest_framework.generics import DestroyAPIView  # Delete
from rest_framework.generics import ListCreateAPIView  # List + create
from rest_framework.generics import RetrieveUpdateAPIView  # Retrieve + update
from rest_framework.generics import RetrieveDestroyAPIView  # Retrieve + delete
from rest_framework.generics import RetrieveUpdateDestroyAPIView  # Retrieve + update + delete

from rest_framework.viewsets import ViewSet  # Custom actions grouped
from rest_framework.viewsets import ModelViewSet  # Full CRUD out of the box
from rest_framework.viewsets import ReadOnlyModelViewSet  # List + retrieve only

from rest_framework import mixins

# Example usage
# class MyView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
#     ...
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
