from django.shortcuts import render
from django.views.generic import *
from .models import *

class OrderList(ListView):
    model = Order
    template_name = "orders/orderlist.html"
    context_object_name = "orders"
