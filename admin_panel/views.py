from django.shortcuts import render


def admin_panel(request):

    """A view that renders the admin panel page"""

    template = 'admin_panel/admin_panel.html'
    page_title = 'Admin Panel'
    context = {
        'page_title': page_title
    }
    return render(request, template, context)
