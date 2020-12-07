from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import modelformset_factory
from django.views.generic import TemplateView, ListView, FormView, UpdateView, DeleteView, DetailView
from django.db.models import Sum, Count
from django.contrib import messages

from extra_views import ModelFormSetView, InlineFormSetFactory, CreateWithInlinesView

from .models import Order, Product, Inventory, Ticket, Shipment, OrderItem
from .forms import InventoryCreateForm, InventoryUpdateForm
from .forms import TicketCreateForm, TicketUpdateForm
from .forms import OrderCreateForm, OrderQuantitiesForm, OrderUpdateForm
from .forms import ShipmentCreateForm, ShipmentUpdateForm

import datetime

# GENERAL
class HomePageView(TemplateView):

    def get_template_names(self):
        if self.request.user.is_staff:
            template_name = 'home.html'
        else:
            template_name = 'landing_page.html'
        return template_name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Context for card counts
        context['total_inventory_items'] = Inventory.objects.count()
        context['total_shipments'] = Shipment.objects.count()
        context['total_tickets'] = Ticket.objects.count()
        context['total_orders'] = Order.objects.count()

        # Context for Order area chart
        sdate = datetime.date.today() - datetime.timedelta(days=7)
        days = []
        order_counts = []
        for i in range(7):
            day = sdate + datetime.timedelta(days=i)
            days.append(str(day.strftime('%b %-d')))
            order_counts.append(Order.objects.filter(order_date__date=day).count())

        context['area_labels'] = days
        context['area_data'] = order_counts

        # Context for Inventory status pie chart
        sum_actual = 0
        sum_planned = 0
        sum_defective = 0
        sum_spoilage = 0

        inventory_queryset = Inventory.objects.all()
        for item in inventory_queryset:
            if item.state == 'Actual':
                sum_actual += item.quantity
            elif item.state == 'Planned':
                sum_planned += item.quantity
            elif item.state == 'Defective':
                sum_defective += item.quantity
            elif item.state == 'Spoilage':
                sum_spoilage += item.quantity

        context['pie_data'] = [sum_actual, sum_planned, sum_defective, sum_spoilage]
        context['pie_labels'] = ['Actual', 'Planned', 'Defective', 'Spoilage']

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

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

class OrderCreateView(FormView):
    form_class = OrderCreateForm
    template_name = 'create_order.html'
    success_url = 'order_quantities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            context['base_template_name'] = 'base_authenticated.html'
        else:
            context['base_template_name'] = 'base.html'
        return context

    def form_valid(self, form):
        self.object = form.save()
        return redirect('order_quantities', pk=self.object.pk)

class OrderQuantitiesView(ModelFormSetView):
    model = OrderItem
    form_class = OrderQuantitiesForm
    template_name = 'order_quantities.html'
    factory_kwargs = {'extra': 0}

    def get_success_url(self):
        if self.request.user.is_staff:
            success_url = '/tickets/'
        else:
            success_url = '/'
        return success_url

    def get_success_url(self):
        order_id = self.kwargs['pk']
        if self.request.user.is_staff:
            success_url = reverse('order_detail', kwargs = {'pk': order_id})
        else:
            success_url = '/'
        return success_url

    def get_queryset(self):
        order_id = self.kwargs['pk']
        queryset = OrderItem.objects.filter(order=order_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            context['base_template_name'] = 'base_authenticated.html'
        else:
            context['base_template_name'] = 'base.html'
        return context

    def formset_valid(self, formset):

        # Iterate through items on order and update Inventory records
        for form in formset:
            # Get Inventory item and pk
            item_pk = form.cleaned_data.get('inventory_item').pk
            item = Inventory.objects.filter(id=item_pk)

            # Update quantity in Inventory table
            quantity_available = item.values('quantity')[0]['quantity']
            quantity_on_order = form.cleaned_data.get('quantity_on_order')
            new_quantity = quantity_available - quantity_on_order
            Inventory.objects.filter(id=item_pk).update(quantity=new_quantity)

            # Update num_orders in Inventory table
            current_num_orders = item.values('num_orders')[0]['num_orders']
            new_num_orders = current_num_orders + 1
            Inventory.objects.filter(id=item_pk).update(num_orders=new_num_orders)

        self.object = formset.save()
        messages.success(self.request, 'Order created successfully.')
        return super().formset_valid(formset)

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderUpdateForm
    success_url = '/orders/'
    template_name = 'create_order.html'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Order updated successfully.')
        return redirect('order_detail', pk=self.object.pk)

class OrderDeleteView(DeleteView):
    model = Order
    success_url = '/orders/'
    success_message = "Order deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(OrderDeleteView, self).delete(self.request, *args, **kwargs)

# SHIPMENTS
class ShipmentsPageView(ListView):
    model = Shipment
    template_name = 'shipments.html'
    context_object_name = 'all_shipments_list'

class ShipmentDetailView(DetailView):
    model = Shipment
    template_name = 'shipment_detail.html'

class ShipmentCreateView(FormView):
    form_class = ShipmentCreateForm
    template_name = 'create_shipment.html'
    success_url = '/shipments/'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Shipment created successfully.')
        return super().form_valid(form)

class ShipmentUpdateView(UpdateView):
    model = Shipment
    form_class = ShipmentUpdateForm
    success_url = '/shipments/'
    template_name = 'create_shipment.html'

    def form_valid(self, form):
        if self.object.status == 'Shipped':
            self.object.shipped_date = datetime.datetime.now()
        self.object = form.save()
        messages.success(self.request, 'Shipment updated successfully.')
        return super().form_valid(form)

class ShipmentDeleteView(DeleteView):
    model = Shipment
    success_url = '/shipments/'
    success_message = "Shipment deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ShipmentDeleteView, self).delete(self.request, *args, **kwargs)

# INVENTORY
class InventoryPageView(ListView):
    model = Inventory
    template_name = 'inventory.html'
    context_object_name = 'all_inventory_list'

class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(items=self.kwargs['pk'])
        context['order_items'] = OrderItem.objects.filter(inventory_item=self.kwargs['pk'])
        return context

class InventoryCreateView(FormView):
    form_class = InventoryCreateForm
    template_name = 'create_inventory.html'
    success_url = '/inventory/'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Inventory created successfully.')
        return super().form_valid(form)

class InventoryUpdateView(UpdateView):
    model = Inventory
    form_class = InventoryUpdateForm
    success_url = '/inventory/'
    template_name = 'create_inventory.html'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Inventory updated successfully.')
        return super().form_valid(form)

class InventoryDeleteView(DeleteView):
    model = Inventory
    success_url = '/inventory/'
    success_message = "Inventory deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(InventoryDeleteView, self).delete(self.request, *args, **kwargs)

# TICKETS
class TicketsPageView(ListView):
    model = Ticket
    template_name = 'tickets.html'
    context_object_name = 'all_tickets_list'

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'ticket_detail.html'

class TicketCreateView(FormView):
    form_class = TicketCreateForm
    template_name = 'create_ticket.html'

    def get_success_url(self):
        if self.request.user.is_staff:
            success_url = '/tickets/'
        else:
            success_url = '/'
        return success_url

    def get_initial(self):
        if 'ticket' in self.request.META['HTTP_REFERER']:
            subsystem = 'Tickets'
        elif 'inventory' in self.request.META['HTTP_REFERER']:
            subsystem = 'Inventory'
        elif 'shipment' in self.request.META['HTTP_REFERER']:
            subsystem = 'Shipments'
        else:
            subsystem = 'Orders'
        return {
            'subsystem': subsystem,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            context['base_template_name'] = 'base_authenticated.html'
        else:
            context['base_template_name'] = 'base.html'
        return context

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Ticket created successfully.')
        return super().form_valid(form)

class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketUpdateForm
    success_url = '/tickets/'
    template_name = 'create_ticket.html'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Ticket updated successfully.')
        return super().form_valid(form)

class TicketDeleteView(DeleteView):
    model = Ticket
    success_url = '/tickets/'
    success_message = "Ticket deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TicketDeleteView, self).delete(self.request, *args, **kwargs)

# AUTHENTICATION
class RegisterPageView(TemplateView):
    template_name = 'register.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class LogoutPageView(TemplateView):
    template_name = 'logout.html'
