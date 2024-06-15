from django.contrib import admin
from .models import ContactForm, Newsletter


class ContactFormAdmin(admin.ModelAdmin):
    readonly_fields = (
        'name',
        'email',
        'date_sent',
        'message',
    )


class NewsletterAdmin(admin.ModelAdmin):
    readonly_fields = (
        'email',
        'date_added',
    )


admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(Newsletter)
