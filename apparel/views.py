from django.shortcuts import render
from .models import Product


def apparel(request):
    """A view to display the products pages """
    products = Product.objects.all()

    return render(request, 'apparel/apparel.html', {'products': products})
