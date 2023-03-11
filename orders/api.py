from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from product.models import Product


class CartApi(generics.GenericAPIView):
    serializer_class = CartSerializer

    def get(self,request,*args, **kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        cart , created = Cart.objects.get_or_create(user=user, cart_status='Inprogress')
        data = CartSerializer(cart).data
        return Response({'cart':data})



class CartDetailCreateApi(generics.GenericAPIView):
    serializer_class = CartDetailSerializer

    def post(self,request,*args, **kwargs):
        cart=Cart.objects.get(user=User.objects.get(username= self.kwargs['username']), cart_status='Inprogress')
        product = Product.objects.get( id=request.data['product_id'])
        cart_data ,created = CartDetail.objects.get_or_create(cart=cart,product=product)  
        cart_data.price = product.price
        cart_data.quantity = int(request.data['quantity'])
        cart_data.total = round(cart_data.quantity * product.price , 2)
        cart_data.save()

        return Response({'status':200})
    

    def delete(self,request,*args, **kwargs):     
        product = Product.objects.get(id=request.data['product_id'])
        cart=Cart.objects.get(user=User.objects.get(username= self.kwargs['username']), cart_status='Inprogress')
        cart_data = CartDetail.objects.get(cart=cart,product=product) 
        cart_data.delete()

        return Response({'status':200,'message':'Deleted Successfully'})
    
  