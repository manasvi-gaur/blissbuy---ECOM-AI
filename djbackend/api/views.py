# from rest_framework import viewsets, routers
# from rest_framework.views import APIView
# from .models import User, Item, Cart, Order
# from .serializers import UserSerializer, ItemSerializer, CartSerializer, OrderSerializer
# from django.http import JsonResponse
# from .predict import predict
# import numpy as np
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.views.decorators.http import require_POST

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

# class CartViewSet(viewsets.ModelViewSet):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

# class FetchItem(APIView):
#     # Product_Category	Customer_Segment	Purchase_History	Competitor_Price	Seasonality	Economic_Indicator	Sentiment	Dynamic_Pricing_Strategy	Revenue	Profitability	Price_Elasticity
#     @method_decorator(require_POST)
#     def post(self, request):
#         user_id = request.data.get("user_id", None)
#         if user_id is None:
#             return JsonResponse({"error":"User ID not found in request!"}, status=400)
#         try:
#             user = User.objects.get(id=user_id)
#         except User.DoesNotExist:
#             return JsonResponse({"error":"User not found!"}, status=404)
        
#         dataset = Item.objects.all()
#         for data in dataset:
#             print(data.seasonality)
#             flag_choice = {"Inactive": 0, "New": 1, "Regular": 2, "Premium": 3}
#             cat_choice = {'Electronics':0, 'Home Appliances':1, 'Clothing':2, 'Health & Beauty':3, "Books": 4}
#             seas_choice = {
#                 "Low":0,
#                 "Medium":1,
#                 "High":2
#             }
#             sent_choice = {
#                 "Negative":-1,
#                 "Neutral":0,
#                 "Positive":1
#             }
#             DPS_choice = {'Dynamic Bundling': 0, 'Dynamic Markdowns': 1, 'Personalized Pricing': 2,'Discounting': 3}
#             pred = np.array([[cat_choice.get(data.cat), flag_choice.get(user.flag), user.purchase_history, data.comp_price, seas_choice.get(data.seasonality), data.eco_ind, sent_choice.get(data.sentiment), DPS_choice.get(data.Dyn_price_strat), data.revenue, data.profitability, data.price_elas]])
            
#             res = predict(pred)
#             print("res: ",res)
#         return JsonResponse({"message":"success"}, status=200)
            

from rest_framework import viewsets, routers
from rest_framework.views import APIView
from .models import User, Item, Cart, Order
from .serializers import UserSerializer, ItemSerializer, CartSerializer, OrderSerializer
from django.http import JsonResponse
from .predict import predict
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class FetchItem(APIView):
    # Product_Category	Customer_Segment	Purchase_History	Competitor_Price	Seasonality	Economic_Indicator	Sentiment	Dynamic_Pricing_Strategy	Revenue	Profitability	Price_Elasticity
    @method_decorator(require_POST)
    def post(self, request):
        user_id = request.data.get("user_id", None)
        if user_id is None:
            return JsonResponse({"error":"User ID not found in request!"}, status=400)
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({"error":"User not found!"}, status=404)
        
        dataset = Item.objects.all()
        for data in dataset:
            flag_choice = {"Inactive": 0, "New": 1, "Regular": 2, "Premium": 3}
            cat_choice = {'Electronics':0, 'Home Appliances':1, 'Clothing':2, 'Health & Beauty':3, "Books": 4}
            seas_choice = {
                "Low":0,
                "Medium":1,
                "High":2
            }
            sent_choice = {
                "Negative":-1,
                "Neutral":0,
                "Positive":1
            }
            print("name: ",data.name)
            DPS_choice = {'Dynamic Bundling': 0, 'Dynamic Markdowns': 1, 'Personalized Pricing': 2,'Discounting': 3}
            pred = np.array([[cat_choice.get(data.cat), flag_choice.get(user.flag), user.purchase_history, data.comp_price, seas_choice.get(data.seasonality), data.eco_ind, sent_choice.get(data.sentiment), DPS_choice.get(data.Dyn_price_strat), data.revenue, data.profitability, data.price_elas]])
            res = predict(pred)
            print("res: ",res)
        return JsonResponse({"message":"success"}, status=200)

