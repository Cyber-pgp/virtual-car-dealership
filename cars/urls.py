from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.home, name='home'),
    path('listings/', views.listings, name='listings'),
    path('cars/<int:car_id>/', views.car_details, name='car_details'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin/dashboard/', views.admindashboard, name='admin_dashboard'),
    path('admin/login/', views.adminlogin, name='adminlogin'),
    path('admin/logout/', views.adminlogout, name='adminlogout'),
    path('save_car/', views.save_car, name='save_car'),
    path('add_car/', views.add_car, name='add_car'),  # Add car route
    path('edit_car/<int:car_id>/', views.edit_car, name='edit_car'),  # Edit car route
    path('delete_car/<int:car_id>/', views.delete_car, name='delete_car'),  # Delete car route
]
