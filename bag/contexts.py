from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from apparel.models import Product, Colour, Size


def bag_contents(request):
    """ Returns the contents of the shopping bag """
    bag_items = []
    total = 0
    item_count = 0
    bag = request.session.get('bag', {})

    for item_key, item_details in bag.items():
        product = get_object_or_404(Product, pk=item_details['item_id'])
        colour = get_object_or_404(Colour, pk=item_details['colour'])
        size = get_object_or_404(Size, pk=item_details['size'])

        item_price = product.discount_price\
            if product.discount\
            else product.price
        total += item_details['quantity'] * item_price

        item_count += item_details['quantity']

        bag_items.append({
            'item_id': item_details['item_id'],
            'quantity': item_details['quantity'],
            'product': product,
            'colour_name': colour.name,
            'size_name': size.name,
            'price': item_price,
            'original_price': product.price,
            'discount_price': product.discount_price
            if product.discount else None,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
