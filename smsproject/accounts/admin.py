from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import CustomUser
from students.models import Student
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'user_type', 'is_staff']
   
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'user_type')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('phone', 'user_type')}),
    )

    admin.site.register(CustomUser)
admin.site.register(Student)