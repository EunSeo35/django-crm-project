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
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'purchases')
    product_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.product_name} - {self.customer.name}"
    
    