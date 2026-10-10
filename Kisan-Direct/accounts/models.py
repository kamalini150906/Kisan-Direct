from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [('farmer', 'Farmer'), ('buyer', 'Buyer')]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')
    phone = models.CharField(max_length=15, blank=True)
    village = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
