from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),   # Maps to the BookList view
]

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs for BookViewSet
]

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # Include other routes for your API
]