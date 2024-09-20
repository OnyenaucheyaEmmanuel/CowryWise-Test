
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserViewSet, BorrowViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)
router.register(r'borrows', BorrowViewSet)

urlpatterns = router.urls