from django.db import models
from account_app.models import Account

class Product(models.Model):
    texture = models.CharField(max_length=50, null=True, default='')
    fabric = models.CharField(max_length=50, null=True, default='')
    shape = models.CharField(max_length=50, null=True, default='')
    part = models.CharField(max_length=50, null=True, default='')
    style = models.CharField(max_length=50, null=True, default='')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img_url = models.CharField(max_length=256, null=True)
    product_url = models.CharField(max_length=256)
    view = models.IntegerField(default=0)

class Rating(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    date = models.DateTimeField('rating date', auto_now=True)
