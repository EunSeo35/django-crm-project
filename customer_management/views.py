from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Customer, Purchase

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'
    
class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['name', 'email', 'phone', 'address']
    success_url = reverse_lazy('customer_management:customer_list') # customer_management/urls.py에서 customer_list라는 이름을 가진 URL 패턴을 찾아서 해당 URL을 반환
 
