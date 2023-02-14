from django.urls import path
from .views import *


app_name = 'product'

urlpatterns = [
    path('',ProductList.as_view(),name='all_products'),
    path('debug',query,name='query'),
    path('<slug:slug>',ProductDetail.as_view(),name='single_product'),
    path('<slug:slug>/add_review',add_review,name='add_review'),
    path('brands/',BrandList.as_view(),name='brand_list'),
    path('brands/<slug:slug>',BrandDetail.as_view(),name='brand_detail'),
]

