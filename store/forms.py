from django import forms
from .models import Product

class uploadform(forms.ModelForm):
    name = forms.CharField()
    price = forms.CharField()
    image = forms.ImageField()
    class Meta:
        model = Product
        fields = ('name', 'price', 'image', 'image')