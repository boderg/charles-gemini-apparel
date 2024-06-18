from django.shortcuts import render


def index(request):

    """A view to display the home page """

    page_title = 'Home'

    return render(request, 'home/index.html', {'page_title': page_title})


def error_404(request, exception):

    """ A view to handle 404 errors"""

    template = '404.html'
    context = {
        'page_title': 'Error 404',
    }

    return render(request, template, context)


def error_500(request):

    """ A view to handle 404 errors"""

    template = '500.html'
    context = {
        'page_title': 'Error 500',
    }

    return render(request, template, context)
