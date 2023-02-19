from django.shortcuts import render
from product.models import Product , Brand ,Reviews
from django.db.models.aggregates import Count



def home(request):
    brands = Brand.objects.annotate(product_count = Count('product_brand'))
    item_sale = Product.objects.filter(flag='Sales')[:10]
    item_feature = Product.objects.filter(flag='Feature')[:6]
    item_new = Product.objects.filter(flag='New')[:12]
    reviews = Reviews.objects.all()[:6]


    context = {
        'brands':brands,
        'item_sale':item_sale,
        'item_feature':item_feature,
        'item_new':item_new,
        'reviews':reviews
    }

    return render(request,'settings/index.html',context)



# You must also create pagination
def sales_products(request):
    sales_products = Product.objects.select_related('brand').filter(flag='Sales')
    return render(request,'settings/sales_products.html',{'sales_products':sales_products})