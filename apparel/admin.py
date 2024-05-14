from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'get_category',
        'price',
        'discount',
        'description',
        'image',
        )

    def get_category(self, obj):
        return ", ".join([category.name for category in obj.category.all()])

    get_category.short_description = 'Category'

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
