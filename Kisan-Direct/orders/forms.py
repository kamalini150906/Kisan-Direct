from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), label='Delivery address')
    class Meta:
        model = Order
        fields = ('quantity', 'address')
