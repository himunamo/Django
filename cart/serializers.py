from django.db.models import fields
from rest_framework import serializers
from .models import *
from products.serializer import *
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'
class CartItemsSerializer(serializers.ModelSerializer):
    cart=CartSerializer()
    product=ProductSerializer()
    class Meta:
        model=CartItems
        fields='__all__'
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields='__all__'