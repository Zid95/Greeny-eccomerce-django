from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *
from django.contrib.auth.models import User


class CartDetailCreateApi(generics.GenericAPIView):

    def get(self,request,*args, **kwargs):
        cart = Cart.objects.get(user=User.objects.get(username = self.kwargs['username']), cart_status = 'Inprogress')
        data = CartSerializer(cart).data
        return Response({'cart':data})

