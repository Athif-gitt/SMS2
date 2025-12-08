from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def student_dashboard(request):
    student = request.user.student  # because of OneToOneField
    return render(request, 'students/dashboard.html', {'student': student})
