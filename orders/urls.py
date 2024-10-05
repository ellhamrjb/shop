from django.urls import path
from .views import CartView, AddToCartView, PlaceOrderView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='add_to_cart'),
    path('order/place/', PlaceOrderView.as_view(), name='place_order'),
]
