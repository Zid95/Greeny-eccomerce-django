from django.shortcuts import render
from django.views.generic import *
from .models import *



class Home(ListView):
    model = Product
    template_name = "index.html"

class ProductList(ListView):
    model = Product
    template_name = 'product/all_products.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/single_product.html'