from django.contrib import admin

from .models import Order, Product, Inventory, Ticket, Shipment
from .forms import InventoryCreateForm, TicketCreateForm, \
    OrderCreateForm, ShipmentCreateForm

class InventoryCreateAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'quantity']
    form = InventoryCreateForm
    search_fields = ['item_name']

class TicketCreateAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    form = TicketCreateForm
    search_fields = ['title', 'description']

class OrderCreateAdmin(admin.ModelAdmin):
    list_display = ['name']
    form = OrderCreateForm
    search_fields = ['name']

class ShipmentCreateAdmin(admin.ModelAdmin):
    list_display = ['name']
    form = ShipmentCreateForm
    search_fields = ['name']

# Register your models here.
admin.site.register(Order, OrderCreateAdmin)
admin.site.register(Shipment, ShipmentCreateAdmin)
admin.site.register(Ticket, TicketCreateAdmin)
admin.site.register(Inventory, InventoryCreateAdmin)
