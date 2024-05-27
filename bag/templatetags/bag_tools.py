from django import template

register = template.Library()


@register.filter(name='item_subtotal')
def item_subtotal(item):

    # Use the discount price if it exists, otherwise use the regular price

    price = item['discount_price']\
        if item['discount_price']\
        else item['product'].price
    return price * item['quantity']
