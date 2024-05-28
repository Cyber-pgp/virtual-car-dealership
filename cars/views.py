# cars/views.py
from django.shortcuts import render
from .models import Car

def car_listings(request):
    return render(request, 'cars/car_listings.html')

def car_detail(request, id):
    car = Car.objects.get(id=id)
    return render(request, 'cars/car_detail.html', {'car': car})
