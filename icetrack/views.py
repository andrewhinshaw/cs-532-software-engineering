from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView

from .models import Order, Product, Inventory, Ticket
from .forms import InventoryCreateForm, TicketCreateForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    total_inventory_items = Inventory.objects.count()
    total_inventory_quantity = Inventory.objects.aggregate(Sum('quantity'))
    total_tickets = Ticket.objects.count()
    total_orders = Order.objects.count()

class OrdersPageView(ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'all_orders_list'

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

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SuccessPageView(TemplateView):
    template_name = 'success.html'

class RegisterPageView(TemplateView):
    template_name = 'register.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class LogoutPageView(TemplateView):
    template_name = 'logout.html'
