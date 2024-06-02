from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Profile
from django.db.models import Q
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser

def is_admin(user):
    if isinstance(user, AnonymousUser):
        return False
    try:
        return user.profile.user_type == 'admin'
    except Profile.DoesNotExist:
        return False

def is_dealer(user):
    if isinstance(user, AnonymousUser):
        return False
    try:
        return user.profile.user_type == 'dealer'
    except Profile.DoesNotExist:
        return False

def is_user(user):
    if isinstance(user, AnonymousUser):
        return False
    try:
        return user.profile.user_type == 'user'
    except Profile.DoesNotExist:
        return False

def home(request):
    return render(request, 'cars/home.html')

def listings(request):
    if request.user.is_authenticated:
        if is_admin(request.user):
            car_list = Car.objects.all()
        elif is_dealer(request.user):
            car_list = Car.objects.filter(added_by=request.user)
        else:
            car_list = Car.objects.filter(available=True)
    else:
        car_list = Car.objects.filter(available=True)
    return render(request, 'cars/car_list.html', {'car_list': car_list})

def car_details(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.user.is_authenticated:
        if is_admin(request.user) or car.added_by == request.user or not is_dealer(request.user):
            return render(request, 'cars/car_details.html', {'car': car})
    return render(request, 'cars/car_details.html', {'car': car})

def search(request):
    query = request.GET.get('q')
    if request.user.is_authenticated:
        if is_admin(request.user):
            cars = Car.objects.filter(Q(make__icontains=query) | Q(model__icontains=query) | Q(fuel__icontains=query))
        elif is_dealer(request.user):
            cars = Car.objects.filter(Q(make__icontains=query) | Q(model__icontains=query) | Q(fuel__icontains=query), added_by=request.user)
        else:
            cars = Car.objects.filter(Q(make__icontains=query) | Q(model__icontains=query) | Q(fuel__icontains=query), available=True)
    else:
        cars = Car.objects.filter(Q(make__icontains=query) | Q(model__icontains=query) | Q(fuel__icontains=query), available=True)
    return render(request, 'cars/search.html', {'cars': cars, 'query': query})

@login_required
def add_car(request):
    if request.method == 'POST':
        make = request.POST['make']
        model = request.POST['model']
        year = request.POST['year']
        fuel = request.POST['fuel']
        mileage = request.POST['mileage']
        engine = request.POST['engine']
        color = request.POST['color']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES.get('image')

        car = Car(
            make=make,
            model=model,
            year=year,
            fuel=fuel,
            mileage=mileage,
            engine=engine,
            color=color,
            price=price,
            description=description,
            image=image,
            added_by=request.user
        )
        car.save()
        return redirect('cars:listings')
    return render(request, 'cars/add_car.html')

@login_required
def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if not (is_admin(request.user) or car.added_by == request.user):
        return redirect('cars:listings')
    if request.method == 'POST':
        car.make = request.POST['make']
        car.model = request.POST['model']
        car.year = request.POST['year']
        car.fuel = request.POST['fuel']
        car.mileage = request.POST['mileage']
        car.engine = request.POST['engine']
        car.color = request.POST['color']
        car.price = request.POST['price']
        car.description = request.POST['description']
        if 'image' in request.FILES:
            car.image = request.FILES['image']
        car.save()
        return redirect('cars:car_details', car_id=car.id)
    return render(request, 'cars/edit_car.html', {'car': car})

@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if not (is_admin(request.user) or car.added_by == request.user):
        return redirect('cars:listings')
    car.delete()
    return redirect('cars:listings')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
 
        if user is not None:
            auth.login(request, user)
            return redirect('cars:dashboard')
        else:
            messages.error(request, 'Oops! Invalid login credentials')
            return redirect('cars:login')
    return render(request, 'cars/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('cars:home')
    return redirect('cars:home')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user_type =   # Added to capture user type

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
                    Profile.objects.create(user=user, user_type=user_type)  # Create Profile with user_type
                    auth.login(request, user)
                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    return redirect('cars:login')
        else:
            messages.error(request, 'Password does not match')
            return redirect('cars:register')
    else:
        return render(request, 'cars/register.html')

@login_required
def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    if profile.user_type == 'admin':
        return redirect('cars:admin_dashboard')
    elif profile.user_type == 'dealer':
        return redirect('cars:dealership_dashboard')
    else:
        return redirect('cars:home')

@login_required
def admindashboard(request):
    if not is_admin(request.user):
        return redirect('cars:home')
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
            if user is not None and is_admin(user):
                login(request, user)
                return redirect('cars:admindashboard')
            else:
                messages.error(request, 'You are not an admin')
                return redirect('cars:home')
    else:
        form = AuthenticationForm()
    return render(request, 'cars/adminlogin.html', {'form': form})

def adminlogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('cars:home')
    return redirect('cars:home')

@login_required
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
             filename = default_storage.save('images/' + img.name, img)
             img_path = default_storage.path(filename)
        else:
            img_path = 'path/to/default/image.jpg'
        car = Car(
            make=car_make,
            model=car_model,
            price=car_price,
            year=car_year,
            mileage=car_mileage,
            engine=car_engine,
            fuel=car_fuel,
            color=car_colour,
            description=car_description,
            image=img_path,
            added_by=request.user  # Associate car with the current user
        )
        car.save()
        return redirect('cars:dashboard')
    else:
        return HttpResponseBadRequest('Invalid Request')
