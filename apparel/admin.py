from django.contrib import admin
from .models import Category, Product, Colour, Size


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'get_colours',
        'get_sizes',
        'price',
        'discount',
        'discount_price',
        'get_category',
        'description',
        'image',
        )

    def get_category(self, obj):
        return ", ".join([category.name for category in obj.category.all()])

    get_category.short_description = 'Category'

    def get_colours(self, obj):
        return ", ".join([colour.name for colour in obj.colours.all()])

    get_colours.short_description = 'Colours'

    def get_sizes(self, obj):
        return ", ".join([size.name for size in obj.sizes.all()])

    get_sizes.short_description = 'Sizes'

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
admin.site.register(Colour)
admin.site.register(Size)
