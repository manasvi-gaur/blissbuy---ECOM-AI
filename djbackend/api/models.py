from django.db import models
import uuid
import djbackend.settings as settings
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, null=False, blank=False, default=uuid.uuid4)
    first_name = models.CharField("First name", max_length=30)
    last_name = models.CharField("Last name", max_length=30)
    email = models.EmailField("Email address")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Item(models.Model):
    catagory = models.CharField()

class Cart(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, null=False, blank=False, default=uuid.uuid4)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    items = models.ManyToManyField(Item)