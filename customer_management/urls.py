from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerUpdateView ,CustomerDeleteView, customer_statistics

app_name = 'customer_management'

urlpatterns = [
    path('list/', CustomerListView.as_view(), name='customer_list'),
    path('list/add',CustomerCreateView.as_view(), name = 'customer_add' ),
    path('<int:pk>/edit/',CustomerUpdateView.as_view(), name = 'customer_edit'), #특정 customer의 pk값 
    path('statistics/', customer_statistics, name='customer_statistics'),
]