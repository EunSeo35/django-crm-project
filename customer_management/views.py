from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Customer, Purchase

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'

