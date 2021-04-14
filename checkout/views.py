from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ISktfAxHa4qHwIHggotPpqkLoVHuaUPYfxIKPKMeG5HwXnzy5DeBRkteLz3SvqtCENQKY7bNZua7A70cVxhhgOg00KbMCz1rT',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
