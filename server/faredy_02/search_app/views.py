from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django import forms
from product_mgr_app.models import Product
from django.db.models import Q

class searchForm(forms.Form):
    attr00 = forms.BooleanField(label='animal', required=False)
    attr01 = forms.BooleanField(label='dot', required=False)
    attr02 = forms.BooleanField(label='floral', required=False)
    attr03 = forms.BooleanField(label='linen', required=False)
    attr04 = forms.BooleanField(label='print', required=False)
    attr05 = forms.BooleanField(label='cotton', required=False)
    attr06 = forms.BooleanField(label='denim', required=False)
    attr07 = forms.BooleanField(label='knit', required=False)
    attr08 = forms.BooleanField(label='neoprene', required=False)
    attr09 = forms.BooleanField(label='nylon', required=False)
    attr10 = forms.BooleanField(label='a-line', required=False)
    attr11 = forms.BooleanField(label='crop', required=False)
    attr12 = forms.BooleanField(label='fit', required=False)
    attr13 = forms.BooleanField(label='muscle', required=False)
    attr14 = forms.BooleanField(label='oversized', required=False)
    attr15 = forms.BooleanField(label='long-sleeve', required=False)
    attr16 = forms.BooleanField(label='off-the-shoulder', required=False)
    attr17 = forms.BooleanField(label='raglan', required=False)
    attr18 = forms.BooleanField(label='sleeve', required=False)
    attr19 = forms.BooleanField(label='sleeveless', required=False)
    attr20 = forms.BooleanField(label='art', required=False)
    attr21 = forms.BooleanField(label='classic', required=False)
    attr22 = forms.BooleanField(label='destroyed', required=False)
    attr23 = forms.BooleanField(label='logo', required=False)
    attr24 = forms.BooleanField(label='sporty', required=False)

def index2_view(request):

    is_POST = False
    if request.method == 'POST':
        is_POST = True
        form = searchForm(request.POST) 
        result = form.changed_data
        return HTTPResponseRedirect('/')
        if form.is_valid():
            clean_data = form.cleaned_data
            request_element = clean_data['element']
            return HTTPResponseRedirect('/')
        else:
            form = searchForm()
            return render(request, 'search_app/index.html', {'form': form})
    else:
        form = searchForm()
        return render(request, 'search_app/index.html', {'form': form})

def index_view(request):
    mapper = {
            'attr00': ('Texture', 'animal'),
            'attr01': ('Texture', 'dot'),
            'attr02': ('Texture', 'floral'),
            'attr03': ('Texture', 'linen'),
            'attr04': ('Texture', 'print'),
            'attr05': ('Fabric', 'cotton'),
            'attr06': ('Fabric', 'denim'),
            'attr07': ('Fabric', 'knit'),
            'attr08': ('Fabric', 'neoprene'),
            'attr09': ('Fabric', 'nylon'),
            'attr10': ('Shape', 'a-line'),
            'attr11': ('Shape', 'crop'),
            'attr12': ('Shape', 'fit'),
            'attr13': ('Shape', 'muscle'),
            'attr14': ('Shape', 'oversized'),
            'attr15': ('Part', 'long-sleeve'),
            'attr16': ('Part', 'off-the-shoulder'),
            'attr17': ('Part', 'raglan'),
            'attr18': ('Part', 'sleeve'),
            'attr19': ('Part', 'sleeveless'),
            'attr20': ('Style', 'art'),
            'attr21': ('Style', 'classic'),
            'attr22': ('Style', 'destroyed'),
            'attr23': ('Style', 'logo'),
            'attr24': ('Style', 'sporty'),
            }
    if request.method == 'POST':
        form = searchForm(request.POST)
        result = form.changed_data
        
        where = [" OR %s = '%s'" % (mapper[attr][0], mapper[attr][1]) for attr in result] 
        if len(where) != 0:
            where[0] = " where " + where[0].strip(" OR")

        query = "SELECT * FROM product_mgr_app_product"
        for condition in where:
            query = query + condition

        query += " ORDER BY view"
        table = Product.objects.raw(query)[:10]
        print("---" * 10)
        print(query)
        print(result)
        print("---" * 10)
        return render(request, 'search_app/index.html', {'is_POST': True, 'form': form, 'table': table})
        #return render(request, 'search_app/index.html', {'is_POST': is_POST, 'from': form, 'result': result, 'records': records})
    else:
        table = Product.objects.all().order_by('-view')[:10]
        form = searchForm()
        return render(request, 'search_app/index.html', {'is_POST': False, 'form': form, 'table': table})
