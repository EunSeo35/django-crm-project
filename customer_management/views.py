from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView #장고에서 제공 
from .models import Customer, Purchase
from django.utils import timezone
from django.db.models import Sum
from datetime import timedelta, date
from django.contrib.auth.mixins import LoginRequiredMixin #로그인 권한 부여 

class CustomerListView(LoginRequiredMixin,ListView): 
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['name', 'gender', 'age', 'email', 'phone', 'address'] # 성별과 나이 필드 추가
    success_url = reverse_lazy('customer_management:customer_list') # customer_management/urls.py에서 customer_list라는 이름을 가진 URL 패턴을 찾아서 해당 URL을 반환
 
class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['name', 'gender', 'age', 'email', 'phone', 'address'] # 성별과 나이 필드 추가
    success_url = reverse_lazy('customer_management:customer_list') 
 
class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer_management:customer_list')
    
    
class CustomerPurchaseDetailView(DetailView):
    model = Customer #고객이 pk
    template_name = 'customer_purchase_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.get_object()
        context['purchases'] = Purchase.objects.filter(customer=customer)
        return context

def customer_statistics(request):
    today = timezone.now().date()
    last_30_days = today - timedelta(days=30)

    # 지난 30일 동안의 구매 총합
    recent_purchases = Purchase.objects.filter(date__gte=last_30_days)
    total_sales = recent_purchases.aggregate(Sum('amount'))['amount__sum'] or 0

    return render(request, 'customer_statistics.html', {
        'total_sales': total_sales,
        'recent_purchases': recent_purchases,
    })
