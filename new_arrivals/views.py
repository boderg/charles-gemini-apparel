from django.shortcuts import render


def new_arrivals(request):
    """A view to display the new arrivals page """

    return render(request, 'new_arrivals/new_arrivals.html')
