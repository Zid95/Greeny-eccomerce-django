from django.urls import path
from .views import *
from .api import *

app_name = "orders"


urlpatterns = [
    path('',OrderList.as_view(),name='order_list'),


    # api
    path('api/<str:username>/cart_',CartApi.as_view(),name='cart_list'),
    path('api/<str:username>/cart_data',CartDetailCreateApi.as_view(),name='cart_list'),
]
