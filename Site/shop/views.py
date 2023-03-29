from django.shortcuts import render, get_object_or_404
from .models import Product_item
# Create your views here.


def index(request):
    return render(request, 'shop/index.html')


def menu(request):
    product_list = Product_item.objects.all()
    data = {
        'product_list': product_list
    }
    return render(request, 'shop/menu.html', data)


def contacts(request):
    return render(request, 'shop/contacts.html')


def bag(requset):
    return render(requset, 'shop/bag.html')


