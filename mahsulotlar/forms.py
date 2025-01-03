from django import forms
from .models import *

from django import forms
from .models import ElektronXizmat

class ElektronXizmatForm(forms.ModelForm):
    class Meta:
        model = ElektronXizmat
        fields = ['nom', 'tavsif', 'narx', 'rasm']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Xizmat nomi'}),
            'tavsif': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Xizmat tavsifi'}),
            'narx': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Xizmat narxi'}),
            'rasm': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class OrderForm(forms.ModelForm):
    class Meta:
        model= Order
        fields="__all__"

    def save(self, commit=True, *args, **kwargs):
        model = super().save(commit=False)
        model.customer = kwargs.get("customer", None)
        if commit:
            model.save()
        return model

class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = "__all__"