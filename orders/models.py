from django.db import models
# from products.models import Product

class Order(models.Model):
    STATE_CHOICES = [
        ('payment_pending', 'Payment Pending'),
        ('paid', 'Paid'),
        ('in_production', 'In Production'),
        ('ready', 'Ready'),
        ('delivered', 'Delivered'),
    ]
    # product_type = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='payment_pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantityRequested = models.IntegerField()
    paid = models.BooleanField(default=False)
    profits = models.IntegerField()

    def __str__(self):
        return str(self.id)
