from django import template
from order.models import Order,OrderProduct
from products.models import Product
register = template.Library()

def check(user, slug):
    queryset = OrderProduct.objects.filter(order__user= user, product__slug= slug, carted=True)
    if queryset.exists():
        
        return True
    return False
register.filter('check',check)