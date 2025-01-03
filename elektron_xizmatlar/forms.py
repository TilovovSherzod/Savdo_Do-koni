from django import forms
from .models import ElektronXizmat

class ElektronXizmatForm(forms.ModelForm):
    """Elektron xizmatlar uchun forma."""
    class Meta:
        model = ElektronXizmat
        fields = ['nom', 'tavsif', 'narx', 'rasm', 'kategoriya']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Xizmat nomi'}),
            'tavsif': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Xizmat tavsifi'}),
            'narx': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Xizmat narxi'}),
            'rasm': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'kategoriya': forms.Select(attrs={'class': 'form-control'}),
        }

class XizmatQidiruvForm(forms.Form):
    """Xizmatlarni qidirish uchun forma."""
    qidiruv_sozi = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qidiruv...'}),
    )
