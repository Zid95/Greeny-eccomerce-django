from rest_framework import serializers
from .models import Product , Brand




class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer()
    brand = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'