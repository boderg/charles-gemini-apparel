from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from apparel.models import Product, Colour, Size
from admin_panel.forms import ProductForm, ColourForm, SizeForm


def admin_panel(request):

    """A view that renders the admin panel page"""

    template = 'admin_panel/admin_panel.html'
    page_title = 'Admin Panel'
    context = {
        'page_title': page_title
    }
    return render(request, template, context)


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
            return redirect(reverse('garment', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add garment. \
                    Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'admin_panel/add_garment.html'
    context = {
        'form': form,
        'page_title': 'Add New Garment',
    }

    return render(request, template, context)


def edit_garment(request, product_id):

    """ A view to edit garments in the store """

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            product.category.set(form.cleaned_data['category'])
            product.colours.set(form.cleaned_data['colours'])
            product.sizes.set(form.cleaned_data['sizes'])
            messages.success(request, 'Garment updated successfully!')
            return redirect(reverse('garment', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update garment. \
                    Please ensure the form is valid.')
    else:
        form = ProductForm(request.POST, request.FILES, instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'admin_panel/edit_garment.html'
    context = {
        'form': form,
        'product': product,
        'page_title': 'Garment Editor',
    }

    return render(request, template, context)


def list_garments(request):

    """ A view to display all the garments """

    products = Product.objects.all()
    page_title = 'Garment Selection'

    template = 'admin_panel/list_garments.html'
    context = {
        'products': products,
        'page_title': page_title,
    }

    return render(request, template, context)


def delete_garment(request, product_id):

    """ A view to delete garments from the store """

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Garment deleted successfully!')
    return redirect(reverse('all_garments'))


def add_colour(request):

    """ A view to add new colours to the store """

    if request.method == 'POST':
        colour_form = ColourForm(request.POST)
        if colour_form.is_valid():
            colour_form.save()
            messages.success(request, 'Colour added successfully!')
            return redirect(reverse('add_colour'))
        else:
            messages.error(
                request, 'Failed to add colour. \
                    Please ensure the form is valid.')
    else:
        colour_form = ColourForm()

    template = 'admin_panel/add_colour.html'
    context = {
        'colour_form': colour_form,
        'page_title': 'Add New Colour',
    }

    return render(request, template, context)


def edit_colour(request, colour_id):

    """ A view to edit colours in the store """

    colour = get_object_or_404(Colour, pk=colour_id)
    if request.method == 'POST':
        colour_form = ColourForm(request.POST, instance=colour)
        if colour_form.is_valid():
            colour_form.save()
            messages.success(request, 'Colour updated successfully!')
            return redirect(reverse('list_colours'))
        else:
            messages.error(
                request, 'Failed to update colour. \
                    Please ensure the form is valid.')
    else:
        colour_form = ColourForm(instance=colour)
        messages.info(request, f'You are editing {colour.name}')

    template = 'admin_panel/edit_colour.html'
    context = {
        'colour_form': colour_form,
        'colour': colour,
        'page_title': 'Colour Editor',
    }

    return render(request, template, context)


def list_colours(request):

    """ A view to display all the colours """

    colours = Colour.objects.all()
    page_title = 'Colour Selection'

    template = 'admin_panel/list_colours.html'
    context = {
        'colours': colours,
        'page_title': page_title,
    }

    return render(request, template, context)


def delete_colour(request, colour_id):
    colour = get_object_or_404(Colour, pk=colour_id)
    colour.delete()
    messages.success(request, 'Colour deleted successfully!')
    return redirect(reverse('list_colours'))


def add_size(request):

    """ A view to add new sizes to the store """

    if request.method == 'POST':
        size_form = SizeForm(request.POST)
        if size_form.is_valid():
            size_form.save()
            messages.success(request, 'Size added successfully!')
            return redirect(reverse('add_size'))
        else:
            messages.error(
                request, 'Failed to add size. \
                    Please ensure the form is valid.')
    else:
        size_form = SizeForm()

    template = 'admin_panel/add_size.html'
    context = {
        'size_form': size_form,
        'page_title': 'Add New Size',
    }

    return render(request, template, context)


def edit_size(request, size_id):

    """ A view to edit sizes in the store """

    size = get_object_or_404(Size, pk=size_id)
    if request.method == 'POST':
        size_form = SizeForm(request.POST, instance=size)
        if size_form.is_valid():
            size_form.save()
            messages.success(request, 'Size updated successfully!')
            return redirect(reverse('list_sizes'))
        else:
            messages.error(
                request, 'Failed to update size. \
                    Please ensure the form is valid.')
    else:
        size_form = SizeForm(instance=size)
        messages.info(request, f'You are editing {size.name}')

    template = 'admin_panel/edit_size.html'
    context = {
        'size_form': size_form,
        'size': size,
        'page_title': 'Size Editor',
    }

    return render(request, template, context)


def list_sizes(request):

    """ A view to display all the sizes """

    sizes = Size.objects.all()
    page_title = 'Size Selection'

    template = 'admin_panel/list_sizes.html'
    context = {
        'sizes': sizes,
        'page_title': page_title,
    }

    return render(request, template, context)


def delete_size(request, size_id):
    size = get_object_or_404(Size, pk=size_id)
    size.delete()
    messages.success(request, 'Size deleted successfully!')
    return redirect(reverse('list_sizes'))
