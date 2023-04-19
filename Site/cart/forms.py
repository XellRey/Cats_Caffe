from django import forms
from cart.models import Product_item


class CartAddProductForm(forms.ModelForm):
    class Meta:
        model = Product_item
        fields = []
