from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)

from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    colour = None
    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']
    cart = request.session.get('cart', {})

    if colour:
        if item_id in list(cart.keys()):
            if colour in cart[item_id]['items_by_colour'].keys():
                cart[item_id]['items_by_colour'][colour] += quantity
                messages.success(
                    request, f'Changed colour of {colour.upper()}'
                             f'{product.part_name} quantity to '
                             f'{cart[item_id]["items_by_colour"][colour]}')
            else:
                cart[item_id]['items_by_colour'][colour] = quantity
                messages.success(
                    request, f'Added {product.part_name} in {colour.upper()}'
                             f' to your cart')
        else:
            cart[item_id] = {'items_by_colour': {colour: quantity}}
            messages.success(
                request, f'Added {product.part_name} in {colour.upper()}'
                         f' to your cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
                request, f'Added another {product.part_name} to your cart')
        else:
            cart[item_id] = quantity
            messages.success(
                request, f'Added {product.part_name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def mod_cart(request, item_id):
    """ Modify the quantity of the specific product to the specific amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    colour = None
    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']
    cart = request.session.get('cart', {})

    if colour:
        if quantity > 0:
            cart[item_id]['items_by_colour'][colour] = quantity
            messages.success(
                request, f'Updated {colour.upper()} {product.part_name}'
                         f' quantity to '
                         f'{cart[item_id]["items_by_colour"][colour]}')

        else:
            del cart[item_id]['items_by_colour'][colour]
            if not cart[item_id]['items_by_colour']:
                cart.pop(item_id)
            messages.success(
                request, f'Removed {product.part_name} in {colour.upper()}'
                         f'from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request, f'Updated {product.part_name} quantity to '
                         f'{cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(
                request, f'Removed {product.part_name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the item from the shopping cart """

    try:
        product = get_object_or_404(Product, pk=item_id)
        colour = None
        if 'product_colour' in request.POST:
            colour = request.POST['product_colour']
        cart = request.session.get('cart', {})

        if colour:
            del cart[item_id]['items_by_colour'][colour]
            if not cart[item_id]['items_by_colour']:
                cart.pop(item_id)
            messages.success(
                request, f'Removed {product.part_name} in {colour.upper()}'
                         f'from your cart')
        else:
            cart.pop(item_id)
            messages.success(
                request, f'Removed {product.part_name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
