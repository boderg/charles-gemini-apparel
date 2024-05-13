from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'price',
        'discount',
        'description',
        'image',
        )

    ordering = (
        'name',
        )


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'friendly_name',
        )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
