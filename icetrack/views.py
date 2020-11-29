from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
from django.db.models import Sum

from .models import Order, Product, Inventory, Ticket, Shipment
from .forms import InventoryCreateForm, TicketCreateForm, \
    OrderCreateForm, ShipmentCreateForm


# Create your views here.
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

class OrdersPageView(ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'all_orders_list'

class OrderCreateView(FormView):
    form_class = OrderCreateForm
    # if form.is_valid(self):
    #     form.save()
    template_name = 'create_order.html'
    success_url = '/orders/'

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

class ShipmentsPageView(ListView):
    model = Shipment
    template_name = 'shipments.html'
    context_object_name = 'all_shipments_list'

class ShipmentCreateView(FormView):
    form_class = ShipmentCreateForm
    # if form.is_valid(self):
    #     form.save()
    template_name = 'create_shipment.html'
    success_url = '/shipments/'

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

class InventoryPageView(ListView):
    model = Inventory
    template_name = 'inventory.html'
    context_object_name = 'all_inventory_list'

class InventoryCreateView(FormView):
    form_class = InventoryCreateForm
    # if form.is_valid(self):
    #     form.save()
    template_name = 'create_inventory.html'
    success_url = '/inventory/'

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

class TicketsPageView(ListView):
    model = Ticket
    template_name = 'tickets.html'
    context_object_name = 'all_tickets_list'

class TicketCreateView(FormView):
    form_class = TicketCreateForm
    # if form.is_valid(self):
    #     form.save()
    template_name = 'create_ticket.html'
    success_url = '/tickets/'

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

class RegisterPageView(TemplateView):
    template_name = 'register.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class LogoutPageView(TemplateView):
    template_name = 'logout.html'
