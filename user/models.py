from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    TYPE_STAFF_CHOICES = (
        ('admin_page', 'Admin'),
        ('seller', 'Seller'),
    )
    phone = models.CharField(max_length=20)
    type_staff  = models.CharField(max_length=20, choices=TYPE_STAFF_CHOICES, default='seller')
    created_at = models.DateTimeField(auto_now_add=True)


