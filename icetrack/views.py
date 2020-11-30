from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.contrib import messages

from .models import Order, Product, Inventory, Ticket, Shipment
from .forms import InventoryCreateForm, InventoryUpdateForm
from .forms import TicketCreateForm, TicketUpdateForm
from .forms import OrderCreateForm, OrderUpdateForm
from .forms import ShipmentCreateForm, ShipmentUpdateForm


# GENERAL
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_inventory_items'] = Inventory.objects.count()
        context['total_shipments'] = Shipment.objects.count()
        context['total_tickets'] = Ticket.objects.count()
        context['total_orders'] = Order.objects.count()
        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SuccessPageView(TemplateView):
    template_name = 'success.html'

# ORDERS
class OrdersPageView(ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'all_orders_list'

class OrderCreateView(FormView):
    form_class = OrderCreateForm
    template_name = 'create_order.html'
    success_url = '/orders/'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Order created successfully.')
        return super().form_valid(form)

class OrderUpdateView(SuccessMessageMixin, UpdateView):
    model = Order
    form_class = OrderUpdateForm
    success_url = '/orders/'
    template_name = 'create_order.html'
    success_message = 'Order updated successfully.'

class OrderDeleteView(SuccessMessageMixin, DeleteView):
    model = Order
    success_url = '/orders/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Order deleted successfully.')
        return super(OrderDeleteView, self).delete(request, *args, **kwargs)

# SHIPMENTS
class ShipmentsPageView(ListView):
    model = Shipment
    template_name = 'shipments.html'
    context_object_name = 'all_shipments_list'

class ShipmentCreateView(FormView):
    form_class = ShipmentCreateForm
    template_name = 'create_shipment.html'
    success_url = '/shipments/'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Shipment created successfully.')
        return super().form_valid(form)

class ShipmentUpdateView(SuccessMessageMixin, UpdateView):
    model = Shipment
    form_class = ShipmentUpdateForm
    success_url = '/shipments/'
    template_name = 'create_shipment.html'
    success_message = 'Shipment updated successfully.'

class ShipmentDeleteView(SuccessMessageMixin, DeleteView):
    model = Shipment
    success_url = '/shipments/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Shipment deleted successfully.')
        return super(ShipmentDeleteView, self).delete(request, *args, **kwargs)

# INVENTORY
class InventoryPageView(ListView):
    model = Inventory
    template_name = 'inventory.html'
    context_object_name = 'all_inventory_list'

class InventoryCreateView(FormView):
    form_class = InventoryCreateForm
    template_name = 'create_inventory.html'
    success_url = '/inventory/'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Inventory created successfully.')
        return super().form_valid(form)

class InventoryUpdateView(SuccessMessageMixin, UpdateView):
    model = Inventory
    form_class = InventoryUpdateForm
    success_url = '/inventory/'
    template_name = 'create_inventory.html'
    success_message = 'Inventory updated successfully.'

class InventoryDeleteView(SuccessMessageMixin, DeleteView):
    model = Inventory
    success_url = '/inventory/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Inventory deleted successfully.')
        return super(InventoryDeleteView, self).delete(request, *args, **kwargs)

# TICKETS
class TicketsPageView(ListView):
    model = Ticket
    template_name = 'tickets.html'
    context_object_name = 'all_tickets_list'

class TicketCreateView(FormView):
    form_class = TicketCreateForm
    template_name = 'create_ticket.html'
    success_url = '/tickets/'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Ticket created successfully.')
        return super().form_valid(form)

class TicketUpdateView(SuccessMessageMixin, UpdateView):
    model = Ticket
    form_class = TicketUpdateForm
    success_url = '/tickets/'
    template_name = 'create_ticket.html'
    success_message = 'Ticket updated successfully.'

class TicketDeleteView(SuccessMessageMixin, DeleteView):
    model = Ticket
    success_url = '/tickets/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Ticket deleted successfully.')
        return super(TicketDeleteView, self).delete(request, *args, **kwargs)

# AUTHENTICATION
class RegisterPageView(TemplateView):
    template_name = 'register.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class LogoutPageView(TemplateView):
    template_name = 'logout.html'
