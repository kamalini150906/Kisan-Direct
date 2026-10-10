from django.conf import settings
from django.db import models

class Product(models.Model):
    CATEGORIES = [('vegetables', 'Vegetables'), ('fruits', 'Fruits'), ('grains', 'Grains & pulses'),
                  ('dairy', 'Dairy & eggs'), ('spices', 'Spices'), ('other', 'Other')]
    UNITS = [('kg', 'per kg'), ('dozen', 'per dozen'), ('piece', 'per piece'), ('litre', 'per litre')]
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORIES, default='vegetables')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=10, choices=UNITS, default='kg')
    quantity = models.PositiveIntegerField(help_text='Stock available')
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
