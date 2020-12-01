from django.db import models
from django.urls import reverse

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    inventory = models.ManyToManyField('Inventory', blank=True)

    def __str__(self):
        return str(self.name)

class Shipment(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    title = models.TextField()

    def __str__(self):
        return str(self.title)

class Inventory(models.Model):
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    received_quantity = models.IntegerField(default='0', blank=True, null=True)
    received_by = models.CharField(max_length=50, blank=True, null=True)
    sold_quantity = models.IntegerField(default='0', blank=True, null=True)
    sold_by = models.CharField(max_length=50, blank=True, null=True)
    sold_to = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
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
