from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserViewSet, BorrowViewSet, sync_book
from django.urls import path


urlpatterns = [
    path('books/sync/', sync_book, name='sync_book'), 
]


router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)
router.register(r'borrows', BorrowViewSet)

urlpatterns += router.urls
