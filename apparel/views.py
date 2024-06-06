from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm


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

    page_title = category[0].friendly_name if category else 'All Designs'

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


def add_garment(request):

    """ A view to add new garments to the store """

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            product.category.set(form.cleaned_data['category'])
            product.colours.set(form.cleaned_data['colours'])
            product.sizes.set(form.cleaned_data['sizes'])
            messages.success(request, 'Garment added successfully!')
            return redirect(reverse('add_garment'))
        else:
            messages.error(
                request, 'Failed to add garment. \
                    Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'apparel/add_garment.html'
    context = {
        'form': form,
        'page_title': 'Product Management',
    }

    return render(request, template, context)
