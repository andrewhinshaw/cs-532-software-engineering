from django import forms
from .models import Inventory, Order, Product

class InventoryCreateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name', 'quantity']

# class OrderCreateForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['item_name', 'quantity']
