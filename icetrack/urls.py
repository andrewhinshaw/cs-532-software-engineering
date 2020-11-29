# icetrack/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, InventoryPageView


# app_name = 'main'  # used for namespacing of urls

urlpatterns = [
    path('about/', AboutPageView.as_view(), name="about"),
    path('inventory/', InventoryPageView.as_view(), name="inventory"),
    path('', HomePageView.as_view(), name="home"),
]
