from django.shortcuts import render


def apparel(request):
    """A view to display the products pages """

    return render(request, 'apparel/apparel.html')
