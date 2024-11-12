from django.urls import path
from .views import CustomerListView

app_name = 'customer_management'

urlpatterns = [
    path('list/', CustomerListView.as_view(), name='customer_list'),
]