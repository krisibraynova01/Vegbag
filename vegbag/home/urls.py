from django.urls import path

from vegbag.home.views import index, add_to_cart

urlpatterns = [
    path('', index, name= "index"),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]