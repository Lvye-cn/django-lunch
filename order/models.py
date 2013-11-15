
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class BaseMixin(models.Model): 
    
    create_at = models.DateTimeField(auto_now=True)

    update_at = models.DateTimeField(auto_now_add=True)
    
    creator = models.ForeignKey(User)
    
    class Meta:
        abstract = True

class Order(BaseMixin):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    expirate_at = models.DateTimeField()
    image = models.ImageField(upload_to='image/%Y/%M/', null=True)

class Fee(BaseMixin):

    order = models.ForeignKey(Order)
    description = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=5, decimal_places=2)
