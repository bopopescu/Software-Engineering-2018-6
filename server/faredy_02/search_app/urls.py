from django.urls import path
from . import views

app_name = 'search_app'
urlpatterns = [
        path('', views.index_view, name='index'),
        #path('test', views.index2_view, name='test'),
        ]
