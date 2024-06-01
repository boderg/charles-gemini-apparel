from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from checkout.models import Order, OrderLineItem
from .forms import OrderForm
from bag.contexts import bag_contents
from apparel.models import Product, Colour, Size

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            bag_contents_data = bag_contents(request)
            order.order_total = bag_contents_data['total']
            order.delivery_cost = bag_contents_data['delivery']
            order.grand_total = bag_contents_data['grand_total']
            order.save()

            # Create order line items
            for item_key, item_details in bag.items():
                product = get_object_or_404(
                    Product, pk=item_details['item_id'])
                colour = get_object_or_404(Colour, pk=item_details['colour'])
                size = get_object_or_404(Size, pk=item_details['size'])
                line_item = OrderLineItem(
                    order=order,
                    product=product,
                    colour=colour,
                    size=size,
                    quantity=item_details['quantity'],
                    lineitem_total=item_details['quantity'] * product.price
                )
                line_item.save()

            request.session['bag'] = {}

            return redirect('checkout_success',
                            order_number=order.order_number)
        else:
            messages.error(request, 'There was an error with your form. \
                           Please double check your information.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request,
                           "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
                         Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'page_title': 'Checkout',
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'order_successful': False
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    order_line_items = order.lineitems.all()

    delivery = order.delivery_cost
    total = order.grand_total

    template = 'checkout/checkout_success.html'
    context = {
        'page_title': 'Checkout Success',
        'order': order,
        'order_line_items': order_line_items,
        'delivery': delivery,
        'total': total,
        'order_successful': True
    }

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}')
    return render(request, template, context)
