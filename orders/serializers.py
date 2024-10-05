from rest_framework import serializers
from .models import Cart,CartItem,Order
from products.models import Product

class CartItemSerializer(serializers.ModelSerializer): #showing the name and price of the products
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', read_only=True, max_digits=10, decimal_places=2)
    
    class Meta:
        model=CartItem
        fields=['id', 'product', 'product_name', 'product_price', 'quantity']
        
class CartSerializer(serializers.ModelSerializer): #Represents the entire cart
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price', 'created_at']
        
    def get_total_price(self, obj):
        return sum([item.product.price * item.quantity for item in obj.items.all()])
    

class OrderSerializer(serializers.ModelSerializer): #Includes details about the Cart and order information
    cart = CartSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'cart', 'total_price', 'ordered_at']
        
