from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_garments(request):

    """A view to display all garments, search queries and sorting """

    products = Product.objects.all()
    query = None
    category = None

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(category__name__in=category)
            category = Category.objects.filter(name__in=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('all_garments'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    page_title = category[0].name if category else 'All Designs'

    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
        'page_title': page_title,
    }

    return render(request, 'apparel/all_garments.html', context)


def garment(request, product_id):

    """A view to display the individual garment page """

    product = get_object_or_404(Product, pk=product_id)
    colours = product.colours.all()
    sizes = product.sizes.all()

    context = {
        'product': product,
        'page_title': product.name,
        'colours': colours,
        'sizes': sizes,
    }

    return render(request, 'apparel/garment.html', context)
