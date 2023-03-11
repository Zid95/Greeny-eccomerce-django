from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from product.models import Product



class OrderListAPI(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
    def list(self, request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        queryset = self.get_queryset().filter(user=user)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

class CreateOrder(generics.GenericAPIView):

    def get(self,request,*args, **kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        cart=Cart.objects.get(user=user, cart_status='Inprogress')
        cart_data = CartDetail.objects.filter(cart=cart)  
    
        new_order = Order.objects.create(user=user)
        for object in cart_data :
            OrderDetail.objects.create(
                order = new_order,
                product = object.product,
                price = object.price,
                quantity = object.quantity,
                total = object.total
            )
        cart.cart_status = 'Completed'
        cart.save()
        return Response({'status':200,'message':'order created successfully'})

class CartDetailCreatApI(generics.GenericAPIView):
    serializer_class = CartDetailSerializer

    def get(self,request,*args, **kwargs):
        user = User.objects.get(username = self.kwargs['username'])
        cart , created = Cart.objects.get_or_create(user=user, cart_status='Inprogress')
        data = CartSerializer(cart).data
        return Response({'cart':data})
    
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
    





  