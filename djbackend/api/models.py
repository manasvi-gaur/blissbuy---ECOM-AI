from django.db import models
import uuid
import djbackend.settings as settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(editable=False, primary_key=True, null=False, blank=False, default=uuid.uuid4)
    first_name = models.CharField("First name", max_length=30)
    last_name = models.CharField("Last name", max_length=30)
    email = models.EmailField("Email address")
    password = models.CharField(max_length=30)
    flag_choice = {"Inactive": 0, "New": 1, "Regular": 2, "Premium": 3}
    flag = models.CharField(choices=flag_choice, default="New", max_length=10)
    purchase_history = models.IntegerField(default=0)
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'password']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Item(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, null=False, blank=False, default=uuid.uuid4)
    cat_choice = {'Electronics':0, 'Home Appliances':1, 'Clothing':2, 'Health & Beauty':3, "Books": 4}
    cat = models.CharField(max_length=30, choices=cat_choice)
    name = models.CharField(max_length=256)
    comp_price = models.IntegerField()
    price = models.IntegerField()
    seas_choice = {
        "Low":0,
        "Medium":1,
        "High":2
    }
    seasonality = models.CharField(choices=seas_choice, max_length=10)
    eco_ind = models.DecimalField(decimal_places=2, max_digits=20)
    sent_choice = {
        "Negative":-1,
        "Neutral":0,
        "Positive":1
    }
    sentiment = models.CharField(choices=sent_choice, default="Neutral", max_length=10)
    DPS_choice = {'Dynamic Bundling': 0, 'Dynamic Markdowns': 1, 'Personalized Pricing': 2,'Discounting': 3}
    Dyn_price_strat = models.CharField(choices=DPS_choice, default="Personalized Pricing", max_length=30)
    revenue = models.IntegerField()
    profitability = models.FloatField()
    price_elas = models.FloatField()

class Cart(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, null=False, blank=False, default=uuid.uuid4)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    items = models.ManyToManyField(Item)

class Order(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, null=False, blank=False, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    items = models.ManyToManyField(Item)
