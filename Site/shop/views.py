from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'shop/index.html')


def menu(request):
    return render(request, 'shop/menu.html')


def contacts(request):
    return render(request, 'shop/contacts.html')
