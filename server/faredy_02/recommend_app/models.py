from django.db import models
from account_app.models import Account
from product_mgr_app.models import Product, Rating

class Recommend(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField('date published')

