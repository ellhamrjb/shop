
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView
from products.views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/products/', include('products.urls')),
    path('api/orders/', include('orders.urls')),
    path('logout/', LogoutView.as_view(next_page='welcome'), name='logout'),
    path('', welcome, name='welcome'),
]


