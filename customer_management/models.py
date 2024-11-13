from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Purchase(models.Model):
    
    CATEGORY_CHOICES = [
        ('1', '카테고리 1'),
        ('2', '카테고리 2'),
        ('3', '카테고리 3'),
        ('4', '카테고리 4'),
        ('5', '카테고리 5'),
        ('6', '카테고리 6'),
        ('7', '카테고리 7'),
        ('8', '카테고리 8'),
        ('9', '카테고리 9'),
        ('10', '카테고리 10'),
        ('11', '카테고리 11'),
        ('12', '카테고리 12'),  ]   
        
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'purchases')
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=50,null=True, blank=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES,null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.product_name} - {self.customer.name}"
    