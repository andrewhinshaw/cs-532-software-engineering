from django.contrib import admin

from .models import Order, Product, Inventory, Ticket
from .forms import InventoryCreateForm

class InventoryCreateAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'quantity']
    form = InventoryCreateForm
    search_fields = ['item_name']

# Register your models here.
admin.site.register(Order)
admin.site.register(Ticket)
admin.site.register(Inventory, InventoryCreateAdmin)
