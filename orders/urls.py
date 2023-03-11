from django.urls import path
from .views import *
from .api import *

app_name = "orders"


urlpatterns = [
    path('',OrderList.as_view(),name='order_list'),


    # api
    path('api/<str:username>/cart',CartDetailCreatApI.as_view(),name='cart'),
    path('api/<str:username>/orders',OrderListAPI.as_view(),name='orders'),
   
    
]
