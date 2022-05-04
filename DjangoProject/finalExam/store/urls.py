from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name= 'main'),
    path('store', views.store, name="store"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout")
]