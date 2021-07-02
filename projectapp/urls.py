from django.urls import path
from projectapp import views
from .views import Register

urlpatterns = [
    # path('index/',views.home, name='index'),
    path('',views.home, name='home'),
    path('index/',views.index),
    path('login/',views.login,name='login'),
    path('register/',Register.as_view(), name='register'),
    path('logout/',views.logout,name='logout'),
    path('account-verify/<slug:token>',views.account_verify, name='account-verify'),
    path('shopdetail',views.shop,name='shopdetail'),
    path('location',views.location,name='location'),
    path('cart',views.cart,name='cart'),



]
