from django.urls import path
from .import views

app_name = 'settings'

urlpatterns = [
    path('',views.home,name='home'),
    path('sales_products',views.sales_products,name='sales_products'),
]
