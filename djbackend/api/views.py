from rest_framework import viewsets
from .models import Cart, CartItem, OrderPlaced
from .serializers import CartSerializer, CartItemSerializer, OrderPlacedSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class OrderPlacedViewSet(viewsets.ModelViewSet):
    queryset = OrderPlaced.objects.all()
    serializer_class = OrderPlacedSerializer
