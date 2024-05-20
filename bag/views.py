from django.shortcuts import render, redirect


def bag(request):

    """ A view that renders the bag contents page """

    page_title = 'Shopping Bag'
    bag = request.session.get('bag', {})

    context = {
        'page_title': page_title,
        'bag': bag,
    }

    return render(request, 'bag/bag.html', context)


def bag_add(request, item_id):

    """Add the specified item and quantity to the shopping bag"""

    quantity = int(request.POST.get('quantity'))
    colour = request.POST.get('colour')
    size = request.POST.get('size')

    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id]['quantity'] += quantity
        if colour and size:
            bag[item_id]['colour'] = colour
            bag[item_id]['size'] = size
    else:
        bag[item_id] = {'quantity': quantity, 'colour': colour, 'size': size}

    request.session['bag'] = bag
    return redirect('bag')


def bag_delete(request):
    pass


def bag_update(request):
    pass
