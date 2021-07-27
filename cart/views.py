from products.models import product
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.



class CartView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self , request):
        user=request.user
        cart=Cart.objects.filter(user=user,ordered=False).first()
        queryset=CartItems.objects.filter(cart=Cart)
        serializers=CartItemsSerializer(queryset,many=True)
        return Response(serializers.data)
    
    def post(self , request):
        data = request.data
        user=request.user
        cart,_ = Cart.objects.get_or_create(user=user, ordered=False)
        Product = product.objects.get(id = data.get('product'))
        price = product.price
        quantity=data.get('quantity')
        cart_items=CartItems(cart=cart,user=user,product=product,price=price,quantity=quantity)
        cart_items.save()
        total_price=0
        cart_items=CartItems.objects.filter(user=user,cart=cart.id)
        for items in cart_items:
            total_price+=items.price
        cart.total_price=total_price
        cart.save()
        return Response({'success':'Items added to your Cart'})
    
    def put(self , request):
        data=request.data
        cart_item=CartItems.objects.get(id=data.get('id'))
        quantity=data.get('quantity')
        cart_item.quantity+=quantity
        cart_item.save()
        return({'success':'Items Updated'})
    
    def delete(self , request):
        user=request.user
        data =request.data
        cart_item=CartItems.objects.grt(id=data.get('id'))
        cart_item.delete()
        cart=Cart.objects.filter(user=user,ordered=False).first()
        queryset=CartItems.objects.filter(cart=Cart)
        serializers=CartItemsSerializer(queryset,many=True)
        return Response(serializers.data)

class OrderAPI(APIView):
    def get(self, request):
        queryset=Orders.objects.filter(user=request.user)
        serializer=OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    
def accounts(request):
    return render(request,'index')