from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import OrderForm
from .models import Order, OrderLineItem
from apparel.models import Product
import json
import time


class StripeWH_Handler:

    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):

        """ Handle a generic/unknown/unexpected webhook event """

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):

        """ Handle the payment_intent.succeeded webhook from Stripe """

        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Create form data from the billing and shipping details
        form_data = {
            'full_name': shipping_details.name,
            'email': billing_details.email,
            'phone_number': shipping_details.phone,
            'street_address1': shipping_details.address.line1,
            'street_address2': shipping_details.address.line2,
            'town_or_city': shipping_details.address.city,
            'county': shipping_details.address.state,
            'postcode': shipping_details.address.postal_code,
            'country': shipping_details.address.country,
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.stripe_pid = pid
            order.original_bag = bag
            order.grand_total = grand_total

            order.save()

            for item_id, item_data in json.loads(bag).items():
                product = get_object_or_404(Product, pk=item_id)
                if isinstance(item_data, int):
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                else:
                    for size, quantity in item_data['items_by_size'].items():
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                            product_size=size,
                        )
                        order_line_item.save()

            return HttpResponse(
                content=f'Webhook received: \
                    {event["type"]} | SUCCESS: Created order in webhook',
                status=200)

        else:
            return HttpResponse(
                content=f'Webhook received: \
                    {event["type"]} | ERROR: Order form is not valid',
                status=500)

    def handle_payment_intent_payment_failed(self, event):

        """ Handle the payment_intent.payment_failed webhook from Stripe """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
