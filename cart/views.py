from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ A a quantity of the specified product to the shopping cart """

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
            else:
                cart[item_id]['items_by_colour'][colour] = quantity
        else:
            cart[item_id] = {'items_by_colour': {colour: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def mod_cart(request, item_id):
    """ Modify the quantity of the specific product to the specific amount """

    quantity = int(request.POST.get('quantity'))
    colour = None
    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']
    cart = request.session.get('cart', {})

    if colour:
        if quantity > 0:
            cart[item_id]['items_by_colour'][colour] = quantity
        else:
            del cart[item_id]['items_by_colour'][colour]
            if not cart[item_id]['items_by_colour']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the item from the shopping cart """

    try:
        colour = None
        if 'product_colour' in request.POST:
            colour = request.POST['product_colour']
        cart = request.session.get('cart', {})

        if colour:
            del cart[item_id]['items_by_colour'][colour]
            if not cart[item_id]['items_by_colour']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
