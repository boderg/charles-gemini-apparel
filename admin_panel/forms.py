from django import forms
from apparel.models import Product, Category, Colour, Size
from django.forms import modelformset_factory

from apparel.models import ProductImage

ProductImageFormSet = modelformset_factory(
        ProductImage, fields=('image',), min_num=5, max_num=5, can_delete=True)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


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
            field.widget.attrs['class'] = 'form-control'


class ColourForm(forms.ModelForm):
    class Meta:
        model = Colour
        fields = ['name', 'swatch']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs[
            'placeholder'] = 'Enter a colour name'
        self.fields['swatch'].widget.attrs[
            'placeholder'] = 'Enter a hex color code'


class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = ['name']
