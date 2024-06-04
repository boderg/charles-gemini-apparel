from django.shortcuts import render


def profile(request):

    """ A view to return the profile page """

    template = 'profiles/profile.html'
    context = {
        'page_title': 'My Profile',
    }

    return render(request, template, context)
