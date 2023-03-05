from rest_framework import serializers
from .models import Product , Brand




class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer()
    brand = serializers.StringRelatedField()
    price_with_tax = serializers.SerializerMethodField()
    # price_with_tax = serializers.SerializerMethodField(method_name='my_func')


    class Meta:
        model = Product
        fields = '__all__'

    def get_price_with_tax(self,product):
        return product.price * 1.1
    

    # def my_func(self,product):
    #     return product.price * 1.1