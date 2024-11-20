from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView #장고에서 제공 
from .models import Customer, Purchase
from django.utils import timezone
from django.db.models import Sum
from datetime import timedelta, date, datetime
from django.contrib.auth.mixins import LoginRequiredMixin #로그인 권한 부여 
from django.db.models.functions import TruncMonth, TruncYear 
from django.db import models
from django.http import JsonResponse
import pandas as pd
from django.db.models import IntegerField, F
from django.db.models.functions import Cast
from django.db.models.functions import ExtractYear
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import CustomerSerializer

class CustomerListAPIView(ListAPIView): #REST API 고객 목록 조회
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerCreateAPIView(CreateAPIView): #REST API 고객 생성
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

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

    # 기본 시작 날짜와 종료 날짜를 설정 (오늘 날짜 기준)
    start_date = today - timedelta(days=30)  # 기본값: 최근 30일
    end_date = today  # 기본값: 오늘

    # URL에서 시작 날짜와 종료 날짜를 받으면 이를 사용
    if 'start_date' in request.GET and 'end_date' in request.GET:
        try:
            start_date = timezone.datetime.strptime(request.GET['start_date'], '%Y-%m-%d').date()
            end_date = timezone.datetime.strptime(request.GET['end_date'], '%Y-%m-%d').date()
        except ValueError:
            # 잘못된 날짜 형식이 들어왔을 경우 예외 처리 (기본값 유지)
            pass

    # 고객 수
    total_customers = Customer.objects.count()

    # 선택된 날짜 범위 동안의 총 판매액
    sales = Purchase.objects.filter(date__gte=start_date, date__lte=end_date).aggregate(Sum('amount'))['amount__sum'] or 0

    # 월별 판매액
    monthly_sales = Purchase.objects.filter(date__gte=start_date, date__lte=end_date) \
        .annotate(month=models.functions.TruncMonth('date')) \
        .values('month') \
        .annotate(total_sales=Sum('amount')) \
        .order_by('month')

    # 연도별 판매액
    yearly_sales = Purchase.objects.filter(date__gte=start_date, date__lte=end_date) \
        .annotate(year=ExtractYear('date')) \
        .values('year') \
        .annotate(total_sales=Sum('amount')) \
        .order_by('year')

    # 카테고리별 판매액
    category_sales = Purchase.objects.values('category') \
        .annotate(total_sales=Sum('amount')) \
        .order_by(Cast('category', IntegerField()))  # category를 숫자로 변환하여 정렬
    
    # 카테고리별 최소 및 최대 판매액 계산
    if category_sales:
        min_sales_category = min(category_sales, key=lambda x: x['total_sales'])
        max_sales_category = max(category_sales, key=lambda x: x['total_sales'])
    else:
        min_sales_category = max_sales_category = None

    # 나이별 판매액
    age_sales = Purchase.objects.values('customer__age') \
        .annotate(total_sales=Sum('amount')) \
        .order_by('customer__age')
    
    # 나이별 최소/최대 판매액 계산
    if age_sales:
        min_sales_age = min(age_sales, key=lambda x: x['total_sales'])
        max_sales_age = max(age_sales, key=lambda x: x['total_sales'])
    else:
        min_sales_age = max_sales_age = None  

    # 성별별 판매액
    gender_sales = Purchase.objects.values('customer__gender') \
        .annotate(total_sales=Sum('amount')) \
        .order_by('customer__gender')

    # 성별별 최소/최대 판매액 계산
    if gender_sales:
        min_sales_gender = min(gender_sales, key=lambda x: x['total_sales'])
        max_sales_gender = max(gender_sales, key=lambda x: x['total_sales'])
    else:
        min_sales_gender = max_sales_gender = None
        
    return render(request, 'customer_statistics.html', {
        # 대시보드 데이터
        'total_customers': total_customers,
        'sales': sales,
        'monthly_sales': monthly_sales,
        'yearly_sales': yearly_sales,
        'category_sales': category_sales,
        'age_sales': age_sales,
        'gender_sales': gender_sales,
        'min_sales_category': min_sales_category,
        'max_sales_category': max_sales_category,
        'min_sales_age': min_sales_age,
        'max_sales_age': max_sales_age,
        'min_sales_gender': min_sales_gender,
        'max_sales_gender': max_sales_gender,
        'start_date': start_date,
        'end_date': end_date,
    })
    
    
def import_csv(request):
    csv_file = './walmart.csv'
    
    # CSV 파일 읽기
    try:
        df = pd.read_csv(csv_file, nrows=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    # 필드 선택 및 나이 매핑
    df = df[['Gender', 'Age', 'Purchase', 'Product_ID', 'Product_Category']]
    age_mapping = {
        '0-17': '10s',
        '18-25': '20s',
        '26-35': '30s',
        '36-45': '40s',
        '46-50': '50s',
        '51-55': '50s',
        '55+': '50s+'
    }

    df['Age'] = df['Age'].map(age_mapping)

    # 데이터베이스에 고객 및 구매 데이터 삽입
    for index, row in df.iterrows():
        name = f"customer{index+1}" 
        email = f"customer{index+1}@example.com"
        phone = "000-0000-0000"  
        address = "LA"  
        
        # 고객 데이터 생성
        customer, created = Customer.objects.get_or_create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            gender=row['Gender'],
            age=row['Age']
        )

        # 구매 데이터 삽입
        Purchase.objects.create(
            customer=customer,
            product_name=f"Product_{row['Product_ID']}",
            product_code=row['Product_ID'],
            category=row['Product_Category'],
            amount=row['Purchase'],
            date=datetime.now().date()
        )

    return JsonResponse({'message': 'CSV data successfully imported'}, status=200)