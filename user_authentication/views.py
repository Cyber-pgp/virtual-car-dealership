from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout

def home(request):
    return render(request, 'user_authentication/home.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # Redirect to a success page.
    else:
        form = AuthenticationForm()
    return render(request, 'user_authentication/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('user_authentication:register')
            elif User.objects.filter(email=email).exists():  # Corrected line
                messages.error(request, 'Email already exists!')
                return redirect('user_authentication:register')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                auth.login(request, user)
                messages.success(request, 'You are now logged in.')
                return redirect('car_listings')  # Adjust this according to your URLs
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('user_authentication:register')
    else:
        return render(request, 'user_authentication/register.html')

def logout(request):
    auth_logout(request)
    messages.info(request, 'You are logged out!')
    return redirect('home')
