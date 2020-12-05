from django import forms
from .models import Inventory, Order, Product, Ticket, Shipment

# INVENTORY
class InventoryCreateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name', 'quantity']

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
        fields = ['item_name', 'quantity']

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
        fields = ['name', 'inventory_items']

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'inventory_items']

# SHIPMENTS
class ShipmentCreateForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['name', 'attached_order']

class ShipmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['name', 'status']
