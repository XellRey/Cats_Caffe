from django.db import models
from django.contrib.contenttypes.models import ContentType
from shop.models import Product_item
from django.contrib.auth.models import User

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,  on_delete=models.CASCADE)
    name = models.CharField(Product_item, max_length=100)
    price = models.DecimalField(Product_item, max_digits=10, decimal_places=2)
    image = models.ImageField(Product_item,)

    def __str__(self):
        return str(self.id)

    def get_cart_items(self):
        return self.Product_item.all()

