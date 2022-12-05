from django.db import models

# Create your models here.
class FoodSales(models.Model):       
    order_date = models.DateField(auto_now_add=True)
    region = models.CharField(max_length=150,null=True)
    city = models.CharField(max_length=100,null=True)    
    category = models.CharField(max_length=100,null=True)
    product = models.CharField(max_length=30,null=True)
    quantity = models.IntegerField(max_length=12,null=True)
    unit_price = models.FloatField()       
                 
    objects = models.Manager()