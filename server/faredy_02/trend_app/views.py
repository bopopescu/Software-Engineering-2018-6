from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django import forms
from .interface import interface
from product_mgr_app.models import Product, Rating

def index_view(request):
    user = request.user
    products = Product.objects.all().order_by('-view')[:10]
    #recommend = interface(1, 10)    # 10 is an arbitrary parameter
    table = products
    return render(request, 'trend_app/index.html', {'table': table})

def detail_view(request, product_id):
    user = request.user
    product = Product.objects.get(pk=product_id)
    product.view += 0
    product.save()

    if user.is_authenticated:
        rating = Rating(account=user.account, product=product, rate=2)
        rating.save()

    return render(request, 'trend_app/detail.html', {'product': product})

