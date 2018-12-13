from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django import forms
from product_mgr_app.models import Product, Rating

class searchForm(forms.Form):
    element = forms.CharField(max_length = 20)

def index_view(request):
    if request.method == 'POST':
        form = searchForm(reqeust.POST) 
        return HTTPResponseRedirect('/')
        if form.is_valid():
            clean_data = form.cleaned_data
            request_element = clean_data['element']
            return HTTPResponseRedirect('/')
        else:
            form = searchForm()
            return render(request, 'community_app/index.html', {'form': form})
    else:
        form = searchForm()
        return render(request, 'community_app/index.html', {'form': form})

