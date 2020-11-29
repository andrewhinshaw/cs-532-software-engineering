from django.contrib import admin

from .models import Order, Product, Inventory, Ticket
from .forms import InventoryCreateForm, TicketCreateForm

class InventoryCreateAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'quantity']
    form = InventoryCreateForm
    search_fields = ['item_name']

class TicketCreateAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    form = TicketCreateForm
    search_fields = ['title', 'description']

# Register your models here.
admin.site.register(Order)
admin.site.register(Ticket, TicketCreateAdmin)
admin.site.register(Inventory, InventoryCreateAdmin)
