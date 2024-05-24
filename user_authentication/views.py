from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return  render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            #return redirect('dashboard')
            #return redirect('/')
            return redirect('cars/car_list.html')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'user_authentication/login.html')

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
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'user_authentication/register.html')

def logout(request):
    auth.logout(request)
    messages.info(request,'You are logged out !')
    return redirect('home')
    