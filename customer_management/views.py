from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from .models import Customer, Purchase

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'



class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')
