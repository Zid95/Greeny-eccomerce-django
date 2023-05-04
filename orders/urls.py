from django.urls import path
from .views import OrderList, add_to_cart, remove_from_Cart, checkout, invoice
from .api import *

app_name = "orders"


urlpatterns = [
    path("", OrderList.as_view(), name="order_list"),
    path("add-to-cart", add_to_cart, name="add_to_cart"),
    path("remove-from-cart/<int:id>", remove_from_Cart, name="remove_from_Cart"),
    path("checkout", checkout, name="checkout"),
    # api
    path("api/<str:username>/cart", CartDetailCreatApI.as_view(), name="cart"),
    path("api/<str:username>/orders", OrderListAPI.as_view(), name="orders"),
    path("api/<str:username>/create_order", CreateOrder.as_view(), name="create_order"),
]
