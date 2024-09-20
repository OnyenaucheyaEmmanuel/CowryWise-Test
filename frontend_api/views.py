from rest_framework import viewsets
from backend_api.models import Book, User, Borrow
from backend_api.serializers import BookSerializer, UserSerializer, BorrowSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.filter(available=True)
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['publisher', 'category']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    @action(detail=False, methods=['post'])
    def borrow(self, request):
        return Response({"message": "Book borrowed successfully."})

@api_view(['POST'])
def sync_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)