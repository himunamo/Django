from rest_framework import serializers
from .models import *


class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityVariant
        fields = '__all__' 
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__' 
    

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    quantity_type = QuantitySerializer()
    class Meta:
        model = product
        #fields = '__all__'
        exclude=['id','product_name']