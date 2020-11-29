from django import forms
from .models import Inventory, Order, Product, Ticket, Shipment

class InventoryCreateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name', 'quantity']

class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name']

class ShipmentCreateForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['name']
