from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    AGE_CHOICES = [
        ('10s', '10s'),
        ('20s', '20s'),
        ('30s', '30s'),
        ('40s', '40s'),
        ('50s+', '50s+'),
    ]
    
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True, null=True)
    age = models.CharField(max_length=10, choices=AGE_CHOICES,blank=True, null=True) 
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Purchase(models.Model):
    
    purchase_choices = [
        ('1', 'category 1'),
        ('2', 'category 2'),
        ('3', 'category 3'),
        ('4', 'category 4'),
        ('5', 'category 5'),
        ('6', 'category 6'),
        ('7', 'category 7'),
        ('8', 'category 8'),
        ('9', 'category 9'),
        ('10', 'category 10'),
        ('11', 'category 11'),
        ('12', 'category 12'),  ]   
        
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'purchases')
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=50,null=True, blank=True)
    category = models.CharField(max_length=2, choices=purchase_choices,null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.product_name} - {self.customer.name}"
    