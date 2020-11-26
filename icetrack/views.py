from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Order


# Create your views here.
class HomePageView(ListView):
    model = Order
    template_name = 'home.html'
    context_object_name = 'all_orders_list'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class RegisterPageView(TemplateView):
    template_name = 'register.html'


class LoginPageView(TemplateView):
    template_name = 'login.html'


class LogoutPageView(TemplateView):
    template_name = 'logout.html'
