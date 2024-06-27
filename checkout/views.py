# All code in this checkout app is created by me,
# with help from the Code Institute's Boutique Ado project.

from django.shortcuts import render, redirect, reverse, \
    get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.db import transaction

from .forms import OrderForm
from .models import Order, OrderLineItem

from apparel.models import Product, Colour, Size
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
                       processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            bag = request.session.get('bag', {})
            if not bag:
                messages.error(
                    request, "There's nothing in your bag at the moment")
                return redirect(reverse('products'))

            try:
                with transaction.atomic():
                    order = order_form.save(commit=False)
                    pid = request.POST.get('client_secret').split('_secret')[0]
                    order.stripe_pid = pid
                    order.original_bag = json.dumps(bag)
                    bag_contents_data = bag_contents(request)
                    order.order_total = bag_contents_data['total']
                    order.delivery_cost = bag_contents_data['delivery']
                    order.grand_total = bag_contents_data['grand_total']
                    order.save()

                    # Save order line items
                    for item_key, item_details in bag.items():
                        product = get_object_or_404(
                            Product, pk=item_details['item_id'])
                        colour = get_object_or_404(
                            Colour, pk=item_details['colour'])
                        size = get_object_or_404(Size, pk=item_details['size'])
                        product_image = product.productimage_set.first()
                        if product_image:
                            image = product_image.image
                        else:
                            image = None
                        OrderLineItem.objects.create(
                            order=order,
                            product=product,
                            colour=colour,
                            size=size,
                            quantity=item_details['quantity'],
                            image=image,
                        )

                    request.session['bag'] = {}
                    request.session['save_info'] = 'save-info' in request.POST
                    return redirect(reverse(
                        'checkout_success', args=[order.order_number]))
            except Exception:
                messages.error(
                    request, 'An error occurred while processing your order. \
                        Please try again.')
                return redirect(reverse('checkout'))

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        if not request.session.get('bag'):
            messages.error(
                request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.create(
            amount=round(bag_contents(request)['grand_total'] * 100),
            currency=settings.STRIPE_CURRENCY,
            metadata={'bag': json.dumps(request.session.get('bag', {}))},
        )

        if request.user.is_authenticated:
            profile = UserProfile.objects.filter(user=request.user).first()
            initial_data = {
                'full_name': request.user.get_full_name,
                'email': request.user.email,
                'phone_number': profile.default_phone_number,
                'country': profile.default_country,
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'county': profile.default_county,
            } if profile else {}
            order_form = OrderForm(initial=initial_data)
        else:
            order_form = OrderForm()

    if not settings.STRIPE_PUBLIC_KEY:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    return render(request, 'checkout/checkout.html', {
        'page_title': 'Checkout',
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
        'order_successful': False
    })


def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        order.user_profile = profile
        order.save()

        if request.session.get('save_info'):
            UserProfileForm({
                'default_full_name': order.full_name,
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }, instance=profile).save()

    messages.success(request, f'Order successfully processed! \
                     Your order number is {order_number}. \
                        A confirmation email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    return render(request, 'checkout/checkout_success.html', {
        'page_title': 'Checkout Success',
        'order': order,
        'order_line_items': order.lineitems.all(),
        'delivery': order.delivery_cost,
        'total': order.grand_total,
        'subtotal': order.order_total,
        'order_successful': True,
    })
