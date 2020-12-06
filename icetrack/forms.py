from django import forms
from django_select2 import forms as s2forms

from .models import Inventory, Order, Product, Ticket, Shipment, OrderItem

# INVENTORY
class InventoryCreateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        labels = {
            'item_name': 'Flavor',
            'package_size': 'Package Size (oz)',
            'created_by': 'Created By'
        }
        fields = ['item_name', 'state', 'quantity', 'package_size', 'created_by']

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required')
        for instance in Inventory.objects.all():
            if instance.item_name == item_name:
                raise forms.ValidationError(str(item_name) + ' is already created')
        return item_name

class InventoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name', 'state', 'quantity']

# TICKETS
class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'subsystem']

class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status']

# ORDERS
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'items']

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['items'].queryset = Inventory.objects.filter(state='Actual', quantity__gt=0)

class OrderQuantitiesForm(forms.ModelForm):
    class Meta:
        fields = ['inventory_item', 'quantity_on_order']

    def __init__(self, *args, **kwargs):
        super(OrderQuantitiesForm, self).__init__(*args, **kwargs)
        self.fields['inventory_item'].disabled = True

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'items']

# SHIPMENTS
class ShipmentCreateForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['name', 'attached_order']

class ShipmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['name', 'status']
