
from rest_framework import viewsets
from .models import Book, User, Borrow
from .serializers import BookSerializer, UserSerializer, BorrowSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    @action(detail=False, methods=['get'])
    def borrowed_books(self, request):
        borrowed = Borrow.objects.all()
        serializer = self.get_serializer(borrowed, many=True)
        return Response(serializer.data)