from django import template
from order.models import Order,OrderProduct


register = template.Library()

def cart_count(user):
    if user.is_authenticated:
        order = Order.objects.filter(user= user)
        
        if order.exists():
            order = order[0]
            qs = order.orderproduct_set.filter(carted=True)
            return qs.count()
    return 0

register.filter('cart_count',cart_count)