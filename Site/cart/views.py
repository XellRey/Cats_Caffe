from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product_item
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.


@require_POST
def CartAdd(request, p_id):
    cart = Cart(request)
    product_item = Product_item.objects.get(id=p_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cart.add(Product_item=product_item)
    return redirect('menu')


def CartRemove(request, product_id):
    cart = Cart(request)
    product = Product_item.objects.get(id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'shop/bag.html', {'cart': cart})
