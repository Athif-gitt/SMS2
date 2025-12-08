from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import EmailAuthenticationForm

def login_user(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)

                if user.user_type == "student":
                    return redirect('students:dashboard')

                if user.user_type == "admin":
                    return redirect('/admin/')

    else:
        form = EmailAuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

    
    