from django.urls import path
from .views import *
from .api import *

app_name = 'product'

urlpatterns = [
    path('',ProductList.as_view(),name='all_products'),
    path('debug',query,name='query'),
    path('<slug:slug>',ProductDetail.as_view(),name='single_product'),
    path('<slug:slug>/add_review',add_review,name='add_review'),
    path('brands/',BrandList.as_view(),name='brand_list'),
    path('brands/<slug:slug>',BrandDetail.as_view(),name='brand_detail'),


    # api urls
    #  (function api url)
    # path('api/list',productlist_api,name='productlist_api'),
    # (class api url)
    path('api/list',ProductListApi.as_view(),name='productlist_api'),  
    path('api/list/brands',BrandListApi.as_view(),name='brandtlist_api'),  
    path('api/list/brands/<slug:slug>',BrandDetailApi.as_view(),name='branddetail_api'),  
    path('api/list/<slug:slug>',ProductDetailApi.as_view(),name='productdetail_api'),  
]

