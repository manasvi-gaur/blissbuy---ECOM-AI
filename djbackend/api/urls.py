from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ItemViewSet, CartViewSet, OrderViewSet, FetchItem

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'items', ItemViewSet)
router.register(r'carts', CartViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('getuser/', FetchItem.as_view()),
]
