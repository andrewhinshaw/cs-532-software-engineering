from django.db import models
from django.urls import reverse

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    inventory_items = models.ManyToManyField('Inventory', blank=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    is_express_shipping = models.BooleanField(default=False, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    shipped_date = models.DateTimeField(blank=True, null=True, auto_now_add=False, auto_now=False)

    def __str__(self):
        return str(self.name)

class Shipment(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    attached_order = models.ForeignKey('Order', on_delete=models.CASCADE, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
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

    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    package_size = models.DecimalField(default='0', blank=True, null=True, \
        max_digits=3, decimal_places=1)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='Planned')
    received_quantity = models.IntegerField(default='0', blank=True, null=True)
    received_by = models.CharField(max_length=50, blank=True, null=True)
    num_orders = models.IntegerField(default='0', blank=True, null=True)
    sold_quantity = models.IntegerField(default='0', blank=True, null=True)
    sold_by = models.CharField(max_length=50, blank=True, null=True)
    sold_to = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    export_to_CSV = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     return reverse('update_inventory', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.item_name)

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('On Hold', 'On Hold'),
        ('Resolved', 'Resolved')
    ]

    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Open')
    opened_by = models.CharField(max_length=50, blank=True, null=True)
    date_opened = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)
