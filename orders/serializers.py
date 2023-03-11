from rest_framework import serializers
from .models import *



class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = ['id','product','price','quantity','total']



class CartSerializer(serializers.ModelSerializer):
    cart_data = CartDetailSerializer(source='cart_detail' ,many=True)
    class Meta:
        model = Cart
        fields = "__all__"


