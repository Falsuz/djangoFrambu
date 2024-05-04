from django.db import models
import uuid

# Create your models here.
# creo que esto ya no sirve pq lo hice en la api
class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 
    
class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATE_CHOICES = [
        ('payment_pending', 'Payment Pending'),
        ('paid', 'Paid'),
        ('in_production', 'In Production'),
        ('ready', 'Ready'),
        ('delivered', 'Delivered'),
    ]

    name = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    product_type = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='payment_pending')
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    paid = models.BooleanField(default=False)
    profits = models.IntegerField()

    def __str__(self):
        return str(self.name)
