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


class OrderDetailSerailizer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'
        
        
class OrderSerializer(serializers.ModelSerializer):
    order_detail = OrderDetailSerailizer(many=True)
    class Meta:
        model = Order
        fields = ['id','order_code','order_status','delivery_date','order_date','order_detail']