from django.shortcuts import render, redirect, get_object_or_404
from .contexts import bag_contents
from django.contrib import messages
from apparel.models import Product, Colour, Size


def bag(request):

    """A view that renders the bag contents page"""

    page_title = 'Shopping Bag'
    context = bag_contents(request)
    context['page_title'] = page_title

    return render(request, 'bag/bag.html', context)


def bag_add(request, item_id):

    """Add the specified item and quantity to the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    colour_id = request.POST.get('colour')
    size_id = request.POST.get('size')

    bag = request.session.get('bag', {})

    # Create a unique key for each combination of item, color, and size
    item_key = f"{item_id}_{colour_id}_{size_id}"

    if item_key in bag:
        bag[item_key]['quantity'] += quantity
    else:
        bag[item_key] = {
            'item_id': item_id, 'quantity': quantity,
            'colour': colour_id, 'size': size_id}
        colour = Colour.objects.get(pk=colour_id)
        size = Size.objects.get(pk=size_id)
    messages.success(request, f'{bag[item_key]["quantity"]} x\
            {product.name} in colour {colour.name} and size {size.name}\
                has been added to your bag.')

    request.session['bag'] = bag
    return redirect('bag')


def bag_update_or_delete(request, item_id):

    """Update or delete the specified item in the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)

        action = request.POST.get('action')
        colour_id = request.POST.get('colour')
        size_id = request.POST.get('size')
        bag = request.session.get('bag', {})

        if action == 'delete':
            try:
                # Find and delete the item
                item_key = f"{item_id}_{colour_id}_{size_id}"
                if item_key in bag:
                    del bag[item_key]
                messages.success(request, f'{product.name}\
                                 has been removed from your bag!')
            except Exception as e:
                messages.error(request, f'Error removing item: {e}')
                return redirect('bag')
        else:
            # Update the item
            quantity = int(request.POST.get('quantity'))
            # Remove the old item entry
            for item_key in list(bag.keys()):
                if item_key.startswith(f"{item_id}_"):
                    del bag[item_key]
                    break
            # Create a new item key
            item_key = f"{item_id}_{colour_id}_{size_id}"
            bag[item_key] = {
                'item_id': item_id,
                'quantity': quantity,
                'colour': colour_id,
                'size': size_id
            }
            colour = Colour.objects.get(pk=colour_id)
            size = Size.objects.get(pk=size_id)
            messages.success(request, f'{bag[item_key]["quantity"]} x\
                {product.name} with colour {colour.name}\
                    and size {size.name} has been updated in your bag.')

        request.session['bag'] = bag
        return redirect('bag')

    except Exception as e:
        messages.error(request, f'Error updating your bag: {e}')
        return redirect('bag')
