from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Check if the email is provided or use the phone number as the username
            if form.cleaned_data['email']:
                user.username = form.cleaned_data['email']
            else:
                user.username = form.cleaned_data['phone_number']
                user.email = None
                # Specify the authentication backend
            authentication_backend = 'authentication.backends.EmailOrPhoneBackend'
            user.backend = authentication_backend
            user.save()
            login(request, user)
            messages.success(request, 'Sign up successful. You are now logged in.')
            return redirect('parking:base')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully.')
                return redirect('parking:base')  # Replace with your desired URL
            else:
                messages.error(request, 'Invalid credentials.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')
