# icetrack/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, InventoryPageView, OrdersPageView, TicketsPageView, InventoryCreateView, SuccessPageView, TicketCreateView


# app_name = 'main'  # used for namespacing of urls

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),

    path('success/', SuccessPageView.as_view(), name="success"),

    path('inventory/', InventoryPageView.as_view(), name="inventory"),
    path('create_inventory/', InventoryCreateView.as_view(), name="create_inventory"),

    path('orders/', OrdersPageView.as_view(), name="orders"),

    path('tickets/', TicketsPageView.as_view(), name="tickets"),
    path('create_ticket/', TicketCreateView.as_view(), name="create_ticket"),

]
