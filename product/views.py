from django.shortcuts import render
from django.views.generic import *
from .models import *



class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product