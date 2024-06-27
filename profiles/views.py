# All code in this profiles app is created by me,
# with help from the Code Institute's Boutique Ado project.

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from checkout.models import Order

from .forms import UserProfileForm


@login_required
def profile(request):

    """ A view to return the profile page """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your profile has been updated successfully')
        else:
            messages.error(
                request, 'Failed to update your profile. \
                    Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'page_title': 'My Profile',
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):

    """ A view to return the order history page """

    order = get_object_or_404(Order, order_number=order_number)
    order_line_items = order.lineitems.all()

    subtotal = order.order_total
    delivery = order.delivery_cost
    total = order.grand_total

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'page_title': 'Order History',
        'order': order,
        'order_line_items': order_line_items,
        'delivery': delivery,
        'total': total,
        'subtotal': subtotal,
        'from_profile': True,
    }

    return render(request, template, context)
