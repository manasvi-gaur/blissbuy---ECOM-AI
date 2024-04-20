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
    flag = models.CharField(max_length=20, blank=True, null=True)
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'password']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Item(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, null=False, blank=False, default=uuid.uuid4)
    catagory = models.CharField(max_length=30)
    name = models.CharField(max_length=256)

class Cart(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, null=False, blank=False, default=uuid.uuid4)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    items = models.ManyToManyField(Item)

class Order(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, null=False, blank=False, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    items = models.ManyToManyField(Item)
