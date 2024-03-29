from django.urls import path

from vegbag.product.views import product

urlpatterns = [
    path('', product, name = 'products')
]