from django.shortcuts import render
from django.db.models import F, Count
from django.db.models.functions import Length, Upper

from django.views.generic import ListView , DetailView, TemplateView
#from .models import Product
from product.models import Product
# Create your views here.

class HomeView(ListView):
    model = Product
    #template_name= 'product/home.html'
    template_name= 'home.html'
    #paginate_by=1 

class ContactView(ListView):
    model = Product
    template_name= 'contact.html'

class ServiceView(ListView):
    model = Product
    #template_name= 'product/service.html'
    template_name= 'service.html'
    #paginate_by=1

class AboutView(ListView):
    model = Product
    #template_name= 'product/service.html'
    template_name= 'about.html'
    #paginate_by=1


class PaymentSystemView(TemplateView):
    template_name = "payment_system.html"

