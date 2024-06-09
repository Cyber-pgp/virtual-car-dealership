from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Car
from .forms import RegisterForm, LoginForm, CarForm

def home(request):
    return render(request, 'cars/home.html')

def listings(request):
    car_list = Car.objects.all()
    return render(request, 'cars/car_list.html', {'car_list': car_list})

def car_details(request, id):  # Ensure 'id' matches the URL pattern
    car = get_object_or_404(Car, id=id)
    return render(request, 'cars/car_details.html', {'car': car})

def search(request):
    query = request.GET.get('q')
    cars = Car.objects.all()
    if query:
        cars = Car.objects.filter(
            Q(make__icontains=query) |
            Q(model__icontains=query) |
            Q(fuel__icontains=query)
        )
    return render(request, 'cars/search.html', {'cars': cars, 'query': query})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars:user_login')
    else:
        form = RegisterForm()
    return render(request, 'cars/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('cars:dashboard')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'cars/login.html', {'form': form})

def user_logout(request):
    auth_logout(request)
    return redirect('cars:home')

@login_required
def dashboard(request):
    car_list = Car.objects.all()
    return render(request, 'cars/dashboard.html', {'car_list': car_list})

@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars:dashboard')
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {'form': form, 'title': 'Add Car'})

@login_required
def admin_dashboard(request):
    num_users = User.objects.exclude(is_superuser=True).count()
    users = User.objects.all()
    context = {'num_users': num_users, 'users': users}
    return render(request, 'cars/admindashboard.html', context)

def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                auth_login(request, user)
                return redirect('cars:admin_dashboard')
            else:
                messages.error(request, 'Invalid credentials or not an admin')
    else:
        form = AuthenticationForm()
    return render(request, 'cars/adminlogin.html', {'form': form})

def admin_logout(request):
    auth_logout(request)
    return redirect('cars:home')

@login_required
def car_edit(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('cars:dashboard')
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car_edit.html', {'form': form})


@login_required
def car_delete(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        car.delete()
        return redirect('cars:dashboard')
    return render(request, 'cars/car_delete.html', {'car': car})

