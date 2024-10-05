from django.contrib import admin
from .models import Cart,CartItem,Order


class CartItemInline(admin.TabularInline):
    model=CartItem
    extra=0
    
class CartAdmin(admin.ModelAdmin):
     list_display = ['user', 'created_at']
     inlines = [CartItemInline]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered_at', 'total_price']

admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)