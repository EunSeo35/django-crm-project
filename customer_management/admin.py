from django.contrib import admin
from .models import Customer, Purchase

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','gender', 'age','email', 'phone','address' ,'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product_name', 'product_code', 'category', 'amount', 'date')
    search_fields = ('customer_name', 'product_name')
    list_filter = ('date',)