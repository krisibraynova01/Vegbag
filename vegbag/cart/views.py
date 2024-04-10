from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from vegbag.cart.forms import DiscountCodeForm
from vegbag.cart.models import CartItem
from decimal import Decimal

@login_required
def view_shopping_cart(request):

    user_cart = request.user.cart


    cart_items = user_cart.cart_item.all()


    for item in cart_items:
        if item.product.is_discount:
            item.discounted_price = item.product.price - (item.product.price * item.product.discount / 100)
        else:
            item.discounted_price = item.product.price


        item.total_price = item.discounted_price * (item.quantity or 0)

        if item.quantity is not None:
            item.total_price = item.discounted_price * item.quantity
        else:
            item.total_price = Decimal('0')


    subtotal = sum(item.total_price for item in cart_items)
    total = subtotal


    discount = 0
    error_message = None

    if request.method == 'POST':
        # Check if it's an update quantity request
        if 'update_quantity' in request.POST:
            try:
                item_id = int(request.POST.get('update_quantity'))
                new_quantity = int(request.POST.get('new_quantity_' + str(item_id)))
                if new_quantity > 0:
                    cart_item = CartItem.objects.get(id=item_id)
                    cart_item.quantity = new_quantity
                    cart_item.save()
                else:
                    messages.error(request, "Quantity must be a positive integer.")
            except (ValueError, CartItem.DoesNotExist):
                messages.error(request, "Invalid quantity update request.")
            return redirect('cart')
        else:
            form = DiscountCodeForm(request.POST)
            if form.is_valid():
                coupon_code = form.cleaned_data['coupon_code']
                if coupon_code == 'VG2':
                    discount = subtotal * Decimal('0.20')
                    total = subtotal - discount
                else:

                    error_message = "Invalid coupon code"
            else:

                error_message = "Invalid coupon code"
    else:
        form = DiscountCodeForm()

    return render(request, 'cart/shopping-cart.html',
                  {'cart_items': cart_items, 'subtotal': subtotal, 'total': total, 'form': form, 'discount': discount,
                   'error_message': error_message})
