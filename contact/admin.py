from django.contrib import admin
from .models import ContactForm, Newsletter


class ContactFormAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'date_sent',
    )


class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'date_added',
    )


admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(Newsletter)
