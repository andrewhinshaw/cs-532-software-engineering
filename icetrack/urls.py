# icetrack/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, SuccessPageView, \
    InventoryPageView, OrdersPageView, ShipmentsPageView, TicketsPageView, \
    InventoryCreateView,  TicketCreateView, \
    OrderCreateView, ShipmentCreateView


# app_name = 'main'  # used for namespacing of urls

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('success/', SuccessPageView.as_view(), name="success"),

    path('inventory/', InventoryPageView.as_view(), name="inventory"),
    path('create_inventory/', InventoryCreateView.as_view(), name="create_inventory"),

    path('orders/', OrdersPageView.as_view(), name="orders"),
    path('create_order/', OrderCreateView.as_view(), name="create_order"),

    path('shipments/', ShipmentsPageView.as_view(), name="shipments"),
    path('create_shipment/', ShipmentCreateView.as_view(), name="create_shipment"),

    path('tickets/', TicketsPageView.as_view(), name="tickets"),
    path('create_ticket/', TicketCreateView.as_view(), name="create_ticket"),
]
