from django.shortcuts import render
from django.views.generic import *
from django.db.models import Count
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
    context_object_name = 'pro'


class BrandList(ListView):
    model = Brand
    queryset = Brand.objects.all().annotate(product_count=Count('product_brand'))
   
    
class BrandDetail(DetailView):
    model = Brand
 