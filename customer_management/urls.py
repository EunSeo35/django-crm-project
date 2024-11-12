from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerDeleteView

app_name = 'customer_management'

urlpatterns = [
    path('list/', CustomerListView.as_view(), name='customer_list'),
    path('list/add',CustomerCreateView.as_view(), name = 'customer_add' ),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    
]