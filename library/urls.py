from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token


router = SimpleRouter()
router.register(r'books', views.BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('signup', views.AuthorSignUp.as_view(), name='signup'),
    path('search/<str:pk>', views.AuthorSearch.as_view(), name='search'),
    path('token', obtain_auth_token, name='api_token_auth'),
]