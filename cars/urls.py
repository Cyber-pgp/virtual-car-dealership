# cars/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_listings, name='car_list'),
    path('<int:id>/', views.car_detail, name='car_detail'),
    path('listings/', views.car_listings, name='car_listings'),
]
