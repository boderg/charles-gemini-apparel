from django import forms
from .models import Product, Category, Colour, Size


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        colours = Colour.objects.all()
        self.fields['colours'].choices = [(c.id, c.name) for c in colours]
        sizes = Size.objects.all()
        self.fields['sizes'].choices = [(s.id, s.name) for s in sizes]
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
