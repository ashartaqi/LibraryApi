from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register(r'authors', views.AuthorViewSet)


urlpatterns = [
    path('', include(router.urls)),
]