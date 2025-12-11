from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from students.models import Student
from django.contrib.auth import logout
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import StudentSignupForm

User = get_user_model()
def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Try logging in with email + password
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            # If user is student → go to their own profile page
            if user.user_type == "student":
                student = Student.objects.get(user=user)
                return redirect('students:profile', id=student.id)

            # If user is admin/staff → send to admin panel
            if user.user_type == "admin" or user.is_staff:
                return redirect('/admin/')

            return redirect('home')

        # If authentication failed
        messages.error(request, "Invalid email or password")
        return redirect('accounts:login')

    return render(request, 'accounts/login.html')



def home(request):
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    return redirect('accounts:login')

User = get_user_model()

def student_signup(request):
    if request.method == "POST":
        form = StudentSignupForm(request.POST, request.FILES)

        if form.is_valid():
            student_obj = form.save(commit=False)

            # Create the CustomUser
            user = User.objects.create_user(
                email=form.cleaned_data['email'],
                username=form.cleaned_data['email'].split("@")[0],
                password=form.cleaned_data['password'],
                user_type='student',
            )

            # link user to student
            student_obj.user = user
            student_obj.save()

            messages.success(request, "Account created! Please log in.")
            return redirect('accounts:login')

        messages.error(request, "Please correct the form errors.")

    else:
        form = StudentSignupForm()

    return render(request, 'accounts/student_signup.html', {'form': form})


    
    