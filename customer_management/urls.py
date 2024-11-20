from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerUpdateView ,CustomerDeleteView,CustomerPurchaseDetailView, customer_statistics
from .views import CustomerAPIView
from . import views
from .views import CustomerListAPIView, CustomerCreateAPIView


app_name = 'customer_management'

urlpatterns = [
    path('list/', CustomerListView.as_view(), name='customer_list'),
    path('list/add',CustomerCreateView.as_view(), name = 'customer_add' ),
    # path('<int:pk>/edit/',CustomerUpdateView.as_view(), name = 'customer_edit'), #특정 customer의 pk값 
    # path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('<int:pk>/edit/',CustomerAPIView.as_view(), name = 'customer_edit'),
    path('<int:pk>/delete/',CustomerAPIView.as_view(), name = 'customer_delete'),
    path('<int:pk>/purchase_detail/', CustomerPurchaseDetailView.as_view(), name='customer_purchase_detail'),
    path('statistics/', customer_statistics, name='customer_statistics'),
    path('csv/', views.import_csv, name='import_csv'), #데이터 삽입 코드 
    path('customers/', CustomerListAPIView.as_view()), #REST API 고객 목록 조회
    path('customers/create/', CustomerCreateAPIView.as_view()), #REST API 고객 생성
]