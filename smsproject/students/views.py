from django.contrib.auth.decorators import login_required
from .models import Student
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


@login_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    return render(request, 'students/dashboard.html', {'student': student})

def student_profile(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'students/profile.html', {'student': student})

@login_required
def my_profile(request):
    student = Student.objects.get(user=request.user)
    return redirect('students:profile', id=student.id)
