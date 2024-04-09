from django.urls import path

from vegbag.cart.views import view_shopping_cart

urlpatterns = [
    path('',view_shopping_cart, name='cart')
]