# icetrack/urls.py
from django.urls import path

from .views import HomePageView, AboutPageView, SuccessPageView
from .views import InventoryPageView, InventoryCreateView, InventoryUpdateView
from .views import OrdersPageView, OrderCreateView, OrderUpdateView
from .views import ShipmentsPageView, ShipmentCreateView, ShipmentUpdateView
from .views import TicketsPageView, TicketCreateView, TicketUpdateView


# app_name = 'main'  # used for namespacing of urls

urlpatterns = [

    # GENERAL
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('success/', SuccessPageView.as_view(), name="success"),

    # INVENTORY
    path('inventory/', InventoryPageView.as_view(), name="inventory"),
    path('create_inventory/', InventoryCreateView.as_view(), name="create_inventory"),
    path('inventory/<int:pk>/update', InventoryUpdateView.as_view(), name="update_inventory"),

    # ORDERS
    path('orders/', OrdersPageView.as_view(), name="orders"),
    path('create_order/', OrderCreateView.as_view(), name="create_order"),
    path('orders/<int:pk>/update', OrderUpdateView.as_view(), name="update_order"),

    # SHIPMENTS
    path('shipments/', ShipmentsPageView.as_view(), name="shipments"),
    path('create_shipment/', ShipmentCreateView.as_view(), name="create_shipment"),
    path('shipments/<int:pk>/update', ShipmentUpdateView.as_view(), name="update_shipment"),

    # TICKETS
    path('tickets/', TicketsPageView.as_view(), name="tickets"),
    path('create_ticket/', TicketCreateView.as_view(), name="create_ticket"),
    path('tickets/<int:pk>/update', TicketUpdateView.as_view(), name="update_ticket"),
]
