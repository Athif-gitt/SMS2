from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', "Student"),
        ('admin', "Admin"),
    ]

    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=30, choices=ROLE_CHOICES, default='student')
    phone = models.CharField(max_length=15, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  

    def __str__(self):
        return self.email
