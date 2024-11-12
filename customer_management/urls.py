from django.urls import path
from .views import CustomerListView, CustomerCreateView

app_name = 'customer_management'

urlpatterns = [
    path('list/', CustomerListView.as_view(), name='customer_list'),
    path('list/add',CustomerCreateView.as_view(), name = 'customer_add' )
]