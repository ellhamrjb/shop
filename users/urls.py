from django.urls import path,include
from .views import UserRegisterView, UserProfileView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
]