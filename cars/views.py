from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car
from django.urls import reverse_lazy
from django.db.models import Q


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
    cars = Car.objects.filter(model__icontains=query) if query else Car.objects.all()
    return render(request, 'cars/search.html', {'cars': cars, 'query': query})
