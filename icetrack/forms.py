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
        fields = ['title', 'description']

class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']

# ORDERS
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name']

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name']

# SHIPMENTS
class ShipmentCreateForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['name']

class ShipmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['name']
