from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car
from django.urls import reverse_lazy
from django.db.models import Q


def home(request):
    car_list = Car.objects.all()
    context = {
        'car_list': car_list,
    }
    return render(request, 'cars/home.html', context)

def listings(request):
    car_list=Car.objects.all()
    context = {
        'car_list':car_list,
    }
    return render(request,'cars/car_list.html',context)

def car_details(request,car_id):
    car=get_object_or_404(Car,pk=car_id)
    context = {
        'car':car,
    }
    return render(request,'cars/car_details.html',context)

def search(request):
    query = request.GET.get('q', '')
    cars = []
    if query:
        cars = Car.objects.filter(Q(make__icontains=query) | Q(model__icontains=query))
    context = {
        'cars': cars,
        'query': query,
    }
    return render(request, 'cars/search.html', context)
