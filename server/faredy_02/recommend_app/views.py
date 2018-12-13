from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django import forms
from .interface import interface
from product_mgr_app.models import Product, Rating

def index_view(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect('/account/login')
    recommend = interface(user.username, 10)    # 10 is an arbitrary parameter
    table = recommend.get_recommend_list()
    if len(table) == 0:
        table = Product.objects.all().order_by('-view')[:10]
    return render(request, 'recommend_app/index.html', {'table': table})

def detail_view(request, product_id):
    user = request.user
    product = Product.objects.get(pk=product_id)
    product.view += 1
    product.save()
    
    if user.is_authenticated:
        rating = Rating(account=user.account, product=product, rate=2)
        rating.save()

    return render(request, 'recommend_app/detail.html', {'product': product})
