# icetrack/urls.py
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import HomePageView, AboutPageView, SuccessPageView
from .views import InventoryPageView, InventoryCreateView, InventoryUpdateView, InventoryDeleteView, InventoryDetailView
from .views import OrdersPageView, OrderCreateView, OrderQuantitiesView, OrderUpdateView, OrderDeleteView, OrderDetailView
from .views import ShipmentsPageView, ShipmentCreateView, ShipmentUpdateView, ShipmentDeleteView, ShipmentDetailView
from .views import TicketsPageView, TicketCreateView, TicketUpdateView, TicketDeleteView, TicketDetailView


# app_name = 'main'  # used for namespacing of urls

urlpatterns = [

    # GENERAL
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('success/', SuccessPageView.as_view(), name="success"),

    # AUTHENTICATION
    path('accounts/', include('registration.backends.default.urls')),

    # INVENTORY
    path('inventory/', InventoryPageView.as_view(), name="inventory"),
    path('create_inventory/', InventoryCreateView.as_view(), name="create_inventory"),
    path('inventory/<int:pk>/update', InventoryUpdateView.as_view(), name="update_inventory"),
    path('inventory/<int:pk>/delete', InventoryDeleteView.as_view(), name="delete_inventory"),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name="inventory_detail"),

    # ORDERS
    path('orders/', OrdersPageView.as_view(), name="orders"),
    path('create_order/', OrderCreateView.as_view(), name="create_order"),
    path('create_order/<int:pk>', OrderQuantitiesView.as_view(), name="order_quantities"),
    path('orders/<int:pk>/update', OrderUpdateView.as_view(), name="update_order"),
    path('orders/<int:pk>/delete', OrderDeleteView.as_view(), name="delete_order"),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name="order_detail"),

    # SHIPMENTS
    path('shipments/', ShipmentsPageView.as_view(), name="shipments"),
    path('create_shipment/', ShipmentCreateView.as_view(), name="create_shipment"),
    path('shipments/<int:pk>/update', ShipmentUpdateView.as_view(), name="update_shipment"),
    path('shipments/<int:pk>/delete', ShipmentDeleteView.as_view(), name="delete_shipment"),
    path('shipments/<int:pk>/', ShipmentDetailView.as_view(), name="shipment_detail"),

    # TICKETS
    path('tickets/', TicketsPageView.as_view(), name="tickets"),
    path('create_ticket/', TicketCreateView.as_view(), name="create_ticket"),
    path('tickets/<int:pk>/update', TicketUpdateView.as_view(), name="update_ticket"),
    path('tickets/<int:pk>/delete', TicketDeleteView.as_view(), name="delete_ticket"),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name="ticket_detail"),

    # WIDGETS
    path("select2/", include("django_select2.urls")),
]
