from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    phone =  models.CharField(max_length=50)
    email =  models.CharField(max_length=50)
    car =  models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

class Item(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500)
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    calories = models.IntegerField(null=True)

class Order(models.Model):
    user_id = models.ForeignKey(User, null=True)
    active = models.BooleanField(default=True)
    price_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
		return "Order id: %s" %(self.id)

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order)
    item_id = models.ForeignKey(Item)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        try:
            return str(self.order.id)
        except:
			return self.orderitem.title
