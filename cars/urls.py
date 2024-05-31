from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.home, name='home'),
    path('listings/', views.listings, name='listings'),  # Changed from 'list' to 'listings'
    path('cars<int:car_id>/', views.car_details, name='car_details'),  # Removed redundant 'cars' prefix
    path('search/', views.search, name='search'),
]
