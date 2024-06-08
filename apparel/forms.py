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


class ColourForm(forms.ModelForm):
    class Meta:
        model = Colour
        fields = ['name']
