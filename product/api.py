from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import *
from .models import *
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filter import ProductFilter



# @api_view(['GET'])
# def productlist_api(request):
#     products = Product.objects.all()[:100]
#     data = ProductSerializer(products,many=True,context = {"request":request}).data 
#     return Response({'data':data})

# list / create
# class ProductListApi(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ProductListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name', 'brand','price','flag']
    filterset_class = ProductFilter


# detail / update / delete 
# class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = "slug"

class ProductDetailApi(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "slug"


class BrandListApi(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    

class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer
    lookup_field = "slug"