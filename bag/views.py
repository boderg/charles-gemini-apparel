from django.shortcuts import render


def bag(request):

    """ A view that renders the bag contents page """

    page_title = 'Shopping Bag'

    context = {
        'page_title': page_title,
    }

    return render(request, 'bag/bag.html', context)
