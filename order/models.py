
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class BaseMixin(models): 
    
    create_at = models.DateTimeField(auto_now=True)

    update_at = models.DateTimeField(auto_now_add=True)
    
    creator = models.ForeignKey(User)


class Order(models):

    expirate_at = models.DateTimeField()
    image = models.ImageField()

class Fee(models):

    order = models.ForeignKey(Order)
    description = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=5, decimal_places=2)
