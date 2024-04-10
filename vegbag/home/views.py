from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from vegbag.blog.models import BlogPost
from vegbag.cart.models import Cart, CartItem
from vegbag.home.forms import AddToCartForm
from vegbag.product.models import Product


# Create your views here.

# Create your views here.
def index(request):
    blog_posts = BlogPost.objects.all()[:3]
    products = Product.objects.all()
    latest_products = Product.objects.order_by('-id')[:3]
    categories = ['All'] + list(Product.objects.values_list('category', flat=True).distinct())

    discounted_products = []
    for product in products:
        if product.is_discount:
            discounted_price = product.price - (product.price * product.discount / 100)
        else:
            discounted_price = product.price

        discounted_products.append({'product': product, 'discounted_price': round(discounted_price, 2)})


    return render(request, 'home/index.html', {'blog_posts': blog_posts,
                                                                   'latest_products':latest_products,
                                                                    'products':products,
                                                                     'categories':categories,
                                                                     'discounted_products': discounted_products
                                               })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(client=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    return redirect('cart')



