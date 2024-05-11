from django.shortcuts import render
from .models import Product


def new(request):
    """A view to display the products pages """
    products = Product.objects.all()
    page_title = 'New Designs'

    return render(request, 'apparel/new.html', {'products': products, 'page_title': page_title})


def tees(request):
    """A view to display the products pages """
    products = Product.objects.all()
    page_title = 'Tees'

    return render(request, 'apparel/tees.html', {'products': products, 'page_title': page_title})