from django.db import models

from django.db import models
from django.conf import settings

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=200)
    roll_number = models.CharField(max_length=50, unique=True)
    email = models.EmailField(null=True, blank=True)
    department = models.CharField(max_length=100)
    year_of_admission = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField()
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.name


