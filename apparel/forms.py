from django import forms
from .models import Product, Category, Colour, Size


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    colours = forms.ModelMultipleChoiceField(
        queryset=Colour.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    sizes = forms.ModelMultipleChoiceField(
        queryset=Size.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
