from django.shortcuts import render, redirect
from .contexts import bag_contents


def bag(request):

    """A view that renders the bag contents page"""

    page_title = 'Shopping Bag'
    context = bag_contents(request)
    context['page_title'] = page_title

    return render(request, 'bag/bag.html', context)


def bag_add(request, item_id):

    """Add the specified item and quantity to the shopping bag"""

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

    request.session['bag'] = bag
    return redirect('bag')


def bag_delete(request):
    pass


def bag_update(request, item_id):

    """Update the specified item's size, color,
        and quantity in the shopping bag"""
    quantity = int(request.POST.get('quantity'))
    colour_id = request.POST.get('colour')
    size_id = request.POST.get('size')

    bag = request.session.get('bag', {})

    # Find the item in the bag
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

    request.session['bag'] = bag
    return redirect('bag')
