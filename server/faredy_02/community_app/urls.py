from django.urls import path
from . import views

app_name = 'community_app'
urlpatterns = [
        path('', views.index_view, name='index'),
        ]
