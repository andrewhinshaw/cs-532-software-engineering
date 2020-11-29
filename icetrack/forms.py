from django import forms
from .models import Inventory, Order, Product, Ticket

class InventoryCreateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name', 'quantity']

class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']
