from django.shortcuts import render ,redirect 
from django.urls import reverse
from django.views.generic import *
from django.db.models import Q , F , Value , Func , ExpressionWrapper ,DecimalField
from django.db.models.aggregates import Sum , Avg ,Max , Min ,Count
from django.db.models.functions import Concat 
from django.http import HttpResponse
from .models import *
from .forms import *


def query(request):

    # data = Product.objects.filter(price = F('quantity') )
    # data = Product.objects.filter(Q(name__contains="Noah") & Q(price__gte = 100))
    # data = Product.objects.order_by('name')[0]
    # data = Product.objects.values_list('id','name').distinct()
    # data = Product.objects.defer("brand")
    # data = Product.objects.select_related('brand').all()
    # data = Product.objects.prefetch_related('brand').all()
    # data = Product.objects.aggregate(brands=Count('brand'))
    # data = Product.objects.annotate(is_new = F("price") * 2)
    # data = Product.objects.annotate(Func(F('name'),Value(' ') 
    # ,F('flag'),function = 'CONCAT'))
    # data = Product.objects.annotate(fullname=Concat('name',Value(" "),'flag'))

    dis_price = ExpressionWrapper(F('price')*.8,output_field=DecimalField())
    data = Product.objects.annotate(discounted_price = dis_price)

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


def add_review(request,slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            if Reviews.objects.filter(user=request.user).exists():
                return HttpResponse("<h1> you have already rating </h1>")
            else:
                myform = form.save(commit=False)
                myform.user = request.user
                myform.product = product
                myform.save()
    return redirect(reverse('product:single_product',kwargs={'slug':slug}))


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