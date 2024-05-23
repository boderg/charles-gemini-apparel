from django import template

register = template.Library()


@register.filter(name='item_subtotal')
def item_subtotal(item):
    return item['product'].price * item['quantity']
