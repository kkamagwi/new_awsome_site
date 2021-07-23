from django import forms
from .models import Tag, Product



class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ('name',)

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('tag', 'price', 'author', 'phone_number', 
                'title', 'body',)
