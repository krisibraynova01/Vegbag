import random

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect

from vegbag.product.forms import ProductForm
from vegbag.product.models import Product


# Create your views here.
def product(request):
    return render(request, 'shop/shop-grid.html')


def some_view(request):
    discounted_products = Product.objects.filter(is_discount=True)

    not_discounted_products = Product.objects.filter(is_discount=False)

    for product in discounted_products:
        discounted_price = product.price - (product.price * product.discount / 100)
        product.discounted_price = round(discounted_price, 2)  # Add discounted_price to the product object
    categories = Product.objects.values_list('category', flat=True).distinct()

    latest_products = Product.objects.order_by('-id')[:3]
    return render(request, 'shop/shop-grid.html', {'not_discounted_products': not_discounted_products,
                                              'discounted_products': discounted_products, 'categories': categories,
                                              'latest_products': latest_products})


def products_by_category(request, category):
    # Fetch discounted products for the selected category
    discounted_products = Product.objects.filter(category=category, is_discount=True)
    not_discounted_products = Product.objects.filter(category=category, is_discount=False)

    # Calculate discounted price for each product
    for product in discounted_products:
        discounted_price = product.price - (product.price * product.discount / 100)
        product.discounted_price = round(discounted_price, 2)

    # Fetch all unique categories
    categories = Product.objects.values_list('category', flat=True).distinct()

    latest_products = Product.objects.order_by('-id')[:3]

    return render(request, 'shop/shop-grid.html',
                  {'discounted_products': discounted_products,
                   'category': category,
                   'categories': categories,
                   'not_discounted_products': not_discounted_products,
                   'latest_products': latest_products})


def details(request, id):
    product = Product.objects.get(pk=id)
    all_products = list(Product.objects.all())
    random.shuffle(all_products)
    random_products = all_products[:4]

    discounted_products = []
    for random_product in random_products:
        if random_product.is_discount:
            discounted_price = random_product.price - (random_product.price * random_product.discount / 100)
        else:
            discounted_price = random_product.price

        discounted_products.append({'product': random_product, 'discounted_price': round(discounted_price, 2)})

    if product.is_discount:
        discounted_price = product.price - (product.price * product.discount / 100)
    else:
        discounted_price = product.price

    discounted_price = round(discounted_price, 2)

    return render(request, 'shop/shop-details.html', {'product': product,
                                                      'random_products': random_products,
                                                      'discounted_products': discounted_products,
                                                      'discounted_price': discounted_price})


@permission_required('vegbag.add_product')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()

    return render(request, 'shop/add_product.html', {'form': form})



