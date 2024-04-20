from rest_framework import serializers
from .models import User, Item, Cart, Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'flag', 'purchase_history']


class ItemSerializer(serializers.ModelSerializer):
    seas_choice = [
        ('Low', 0),
        ('Medium', 1),
        ('High', 2)
    ]
    sent_choice = [
        ('Negative', -1),
        ('Neutral', 0),
        ('Positive', 1)
    ]
    DPS_choice = [
        ('Dynamic Bundling', 0),
        ('Dynamic Markdowns', 1),
        ('Personalized Pricing', 2),
        ('Discounting', 3)
    ]

    seasonality = serializers.ChoiceField(choices=seas_choice)
    sentiment = serializers.ChoiceField(choices=sent_choice, default='Neutral')
    Dyn_price_strat = serializers.ChoiceField(choices=DPS_choice, default='Personalized Pricing')

    class Meta:
        model = Item
        fields = ['id', 'cat', 'name', 'comp_price', 'price', 'seasonality', 'eco_ind', 'sentiment', 'Dyn_price_strat', 'revenue', 'profitability', 'price_elas']


class CartSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'owner', 'items']

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'items']
