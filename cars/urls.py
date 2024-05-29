from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.listings, name='listings'),
    path('cars/<int:car_id>/', views.car_details, name='car_details'),
    path('search/', views.search, name='search'),
]
