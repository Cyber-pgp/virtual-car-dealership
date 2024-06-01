from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import default_storage
#from django.contrib.auth.decorators import user_passes_test


def home(request):
    return render(request, 'cars/home.html')

def listings(request):
    car_list = Car.objects.all()
    return render(request, 'cars/car_list.html', {'car_list': car_list})

def car_details(request, car_id):
    car = Car.objects.get(id=car_id)
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
    else:
        cars = []
    return render(request, 'cars/search.html', {'cars': cars, 'query': query})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
 
        if user is not None:
            auth.login(request, user)
            #messages.success(request, 'You are now logged in.')
            return redirect('cars:dashboard')
        else:
            messages.error(request,'Oops! Invalid login credentials')
            return redirect('cars:login')
    return render(request, 'cars/login.html')
 
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')
 
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
                return redirect('cars:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('cars:register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    return redirect('cars:login')
        else:
            messages.error(request, 'Password does not match')
            return redirect('cars:register')
    else:
        return render(request, 'cars/register.html')
   
def dashboard(request):
    return render(request,'cars/dashboard.html')
 
 
 
def admindashboard(request):
    num_users = User.objects.exclude(is_superuser=True).count()
    context = {'num_users': num_users}
    return render(request, 'cars/admindashboard.html', context)
 
 
 
 
def adminlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                login(request)
                return redirect('cars:admindashboard')
            else:
                messages.error(request, 'you are not ad admin')
                return redirect('cars:home')
    else:
        form = AuthenticationForm()
    return render(request, 'cars/adminlogin.html', {'form': form})
 
def adminlogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('cars:home')
    return redirect('cars:home')
 
def save_car(request):
    if request.method == 'POST':
        car_make = request.POST['make']
        car_model = request.POST['model']
        car_price = request.POST['price']
        car_year = request.POST['year']
        car_mileage = request.POST['mileage']
        car_engine = request.POST['engine']
        car_fuel = request.POST['fuel']
        car_colour  = request.POST['color']
        img = request.FILES['image']
        car_description = request.POST['description']
        if img:
             filename = default_storage.save('images/'+ img.name, img)
             img_path = default_storage.path(filename)
        else:
            img_path='path/to/default/image.jpg'
        car = Car(make= car_make,model=car_model,price=car_price,year=car_year,mileage=car_mileage,engine=car_engine, fuel=car_fuel,color=car_colour,description=car_description, image=img_path)
        car.save()
        return redirect('cars:dashboard')
    else:
        return HttpResponseBadRequest('Invalid Request')
        