from django.shortcuts import render
from django.views.generic import *
from django.db.models import Count
from django.db.models import Q , F
from .models import *


def query(request):
    # data = Product.objects.filter(price = F('quantity') )
    # data = Product.objects.filter(Q(name__contains="Noah") & Q(price__gte = 100))
    # data = Product.objects.order_by('name')[0]
    # data = Product.objects.values_list('id','name').distinct()
    # data = Product.objects.defer("brand")
    # data = Product.objects.select_related('brand').all()
    data = Product.objects.prefetch_related('brand').all()
   
    
    return render(request,'product/query.html',{'data':data})


class Home(ListView):
    model = Product
    template_name = "index.html"

class ProductList(ListView):
    model = Product
    template_name = 'product/all_products.html'
    context_object_name = 'products'
    paginate_by = 50



class ProductDetail(DetailView):
    model = Product
    template_name = 'product/single_product.html'
    context_object_name = 'pro'


class BrandList(ListView):
    model = Brand
    queryset = Brand.objects.all().annotate(product_count=Count('product_brand'))
    paginate_by = 25


   
    
class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'
    context_object_name = 'products'
    paginate_by = 25
    
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = (Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand')))[0]
        return context