from django.shortcuts import render


def index(request):

    """A view to display the home page """

    page_title = 'Home'

    return render(request, 'home/index.html', {'page_title': page_title})
