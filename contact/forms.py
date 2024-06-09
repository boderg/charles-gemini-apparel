from django import forms
from .models import ContactForm, Newsletter


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter your name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['message'].widget.attrs[
            'placeholder'] = 'Enter your message'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
