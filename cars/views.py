# cars/views.py
from django.shortcuts import render
from .models import Car

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, id):
    car = Car.objects.get(id=id)
    return render(request, 'cars/car_detail.html', {'car': car})
