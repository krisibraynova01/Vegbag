from django.urls import path

from vegbag.product.views import product, some_view, products_by_category, details, add_product

urlpatterns = [
    path('', some_view, name = 'products'),
    path('details/<int:id>/', details, name='shop_details'),
    path('<str:category>/', products_by_category, name='products_by_category'),
    path('add/', add_product, name='add_product'),
]