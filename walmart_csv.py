import os, sys
import django
import pandas as pd
from datetime import datetime


# Django 환경 설정 초기화
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  
django.setup()

from customer_management.models import Customer, Purchase

print("Django settings configured:", django.conf.settings.configured)

df = pd.read_csv('./walmart.csv', nrows=500)
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



# 임의로 고객 데이터 생성
for index, row in df.iterrows():
    name = f"customer{index+1}" 
    email = f"customer{index+1}@example.com"
    phone = "000-0000-0000"  
    address = "LA"  
    
    # Customer 객체 생성 (없으면 새로 생성)
    customer, created = Customer.objects.get_or_create(
        name=name,
        email=email,
        phone=phone,
        address=address,
        gender=row['Gender'],
        age=row['Age']
    )

    # Purchase 테이블에 데이터 삽입
    Purchase.objects.create(
        customer=customer,
        product_name=f"Product_{row['Product_ID']}",  # 제품 이름 임의 생성
        product_code=row['Product_ID'],  # Product_ID를 product_code로 사용
        category=row['Product_Category'],  # Product_Category 그대로 사용
        amount=row['Purchase'],  # Purchase 값은 amount로 사용
        date=datetime.now().date()  # 날짜는 현재 날짜로 설정
    )

print("Success")