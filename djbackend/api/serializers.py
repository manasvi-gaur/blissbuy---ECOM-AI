from rest_framework import serializers
from .models import Cart, CartItem, OrderPlaced

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product_name', 'quantity', 'price']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'items']

class OrderPlacedSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = OrderPlaced
        fields = ['id', 'user', 'items', 'total_amount', 'placed_at']
