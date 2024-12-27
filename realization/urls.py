from django.urls import path
from knox import views as knox_views
from .views import HomeView, UserRegisterationAPIView, UserLoginAPIView, UserLogoutAPIView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('sign_up/', UserRegisterationAPIView.as_view(), name='sign_up'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout')
]
