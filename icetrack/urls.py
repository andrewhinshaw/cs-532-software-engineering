# icetrack/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView


# app_name = 'main'  # used for namespacing of urls

urlpatterns = [
    path('about/', AboutPageView.as_view(), name="about"),
    path('', HomePageView.as_view(), name="home"),
]
