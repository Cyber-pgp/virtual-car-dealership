from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car
from django.urls import reverse_lazy
from .forms import CarForm

class CarListView(ListView):
    model = Car
    template_name = 'cars/car_listings.html'
    context_object_name = 'cars'

def car_listings(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_listings.html', {'cars': cars})

def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, 'cars/car_detail.html', {'car': car})

class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('car_listings')

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('car_listings')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars/car_confirm_delete.html'
    success_url = reverse_lazy('car_listings')