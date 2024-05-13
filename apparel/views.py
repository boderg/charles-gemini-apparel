from django.shortcuts import render, get_object_or_404
from .models import Product


# def new(request):
#     """A view to display the new designs page """
#     products = Product.objects.all()
#     page_title = 'New Designs'

#     return render(request, 'apparel/new.html',
#                   {'products': products, 'page_title': page_title})


# def tees(request):
#     """A view to display the tees page """
#     products = Product.objects.all()
#     page_title = 'Tees'

#     return render(request, 'apparel/tees.html',
#                   {'products': products, 'page_title': page_title})


# def hoodies(request):
#     """A view to display the hoodies page """
#     products = Product.objects.all()
#     page_title = 'Hoodies'

#     return render(request, 'apparel/hoodies.html',
#                   {'products': products, 'page_title': page_title})


def all_garments(request):

    """A view to display all garments, search queries and sorting """

    products = Product.objects.all()

    context = {
        'products': products,
        'page_title': 'All Designs',
    }

    return render(request, 'apparel/all_garments.html', context)


def garment(request, product_id):

    """A view to display the individual garment page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'page_title': product.name,
    }

    return render(request, 'apparel/garment.html', context)
