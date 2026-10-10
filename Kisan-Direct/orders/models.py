from django.conf import settings
from django.db import models
from products.models import Product

class Order(models.Model):
    STATUS = [('pending', 'Pending'), ('confirmed', 'Confirmed'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')]
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    address = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
