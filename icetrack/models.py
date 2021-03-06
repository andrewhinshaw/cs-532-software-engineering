from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
        ('Placed', 'Placed'),
        ('Fulfilled', 'Fulfilled'),
        ('Canceled', 'Canceled'),
    ]

    name = models.CharField(max_length=50, blank=True, null=True)
    items = models.ManyToManyField('Inventory', blank=True, through='OrderItem')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Placed')
    order_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    inventory_item = models.ForeignKey('Inventory', on_delete=models.CASCADE)
    quantity_on_order = models.IntegerField(default='0', blank=True, null=True)
    submitted = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return str(self.quantity_on_order)

class Shipment(models.Model):
    STATUS_CHOICES = [
        ('Unshipped', 'Unshipped'),
        ('Shipped', 'Shipped'),
        ('Lost', 'Lost'),
        ('Delayed', 'Delayed'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
    ]

    name = models.CharField(max_length=50, blank=True, null=True)
    attached_order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Unshipped')
    is_express_shipping = models.BooleanField(default=False, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    shipped_date = models.DateTimeField(blank=True, null=True, auto_now_add=False, auto_now=False)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    title = models.TextField()

    def __str__(self):
        return str(self.title)

class Inventory(models.Model):
    STATE_CHOICES = [
        ('Actual', 'Actual'),
        ('Planned', 'Planned'),
        ('Spoilage', 'Spoilage'),
        ('Defective', 'Defective'),
    ]

    item_name = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    package_size = models.IntegerField(default='0', blank=True, null=True)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='Planned')
    received_quantity = models.IntegerField(default='0', blank=True, null=True)
    received_by = models.CharField(max_length=50, blank=True, null=True)
    num_orders = models.IntegerField(default='0', blank=True, null=True)
    sold_quantity = models.IntegerField(default='0', blank=True, null=True)
    sold_by = models.CharField(max_length=50, blank=True, null=True)
    sold_to = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True, default='Administrator')
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return str(self.item_name)

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('On Hold', 'On Hold'),
        ('Resolved', 'Resolved')
    ]
    SUBSYSTEM_CHOICES = [
        ('N/A', 'N/A'),
        ('Dashboard', 'Dashboard'),
        ('Orders', 'Orders'),
        ('Inventory', 'Inventory'),
        ('Shipments', 'Shipments'),
        ('Tickets', 'Tickets'),
    ]

    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Open')
    subsystem = models.CharField(max_length=10, choices=SUBSYSTEM_CHOICES, default='N/A')
    opened_by = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_opened = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)
