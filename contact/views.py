from django.shortcuts import render, redirect
from .forms import ContactForm, NewsletterForm
from django.contrib import messages


def contact(request):

    """ View to display contact page """

    page_title = 'Contact'
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('contact_success')
    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'page_title': page_title,
        'contact_form': contact_form
    }
    return render(request, template, context)


def contact_success(request):

    """ View to display contact success page """

    page_title = 'Contact Success'
    template = 'contact/contact_success.html'
    context = {
        'page_title': page_title
    }
    return render(request, template, context)
