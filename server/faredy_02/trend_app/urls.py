from django.urls import path
from . import views

app_name = 'trend_app'
urlpatterns = [
        path('', views.index_view, name='index'),
        path('<int:product_id>/', views.detail_view, name='detail'),
        #path('/<int:P_SN>/buy', views.buy_view, name='buy'),
        ]
