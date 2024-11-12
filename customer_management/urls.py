from django.urls import path
from .views import CustomerListView, CustomerDeleteView

app_name = 'customer_management'

urlpatterns = [
    path('list/', CustomerListView.as_view(), name='customer_list'),

    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
]