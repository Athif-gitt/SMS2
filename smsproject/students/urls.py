from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('profile/', views.my_profile, name='my_profile'),
    path('<int:id>/', views.student_profile, name='profile'),
]
