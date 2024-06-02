from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.home, name='home'),
    path('listings/', views.listings, name='listings'),
    path('car/<int:id>/', views.car_details, name='car_details'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admindashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('adminlogout/', views.admin_logout, name='admin_logout'),
    path('car/add/', views.add_car, name='car_add'),
    path('car/edit/<int:id>/', views.car_edit, name='car_edit'),
    path('car/delete/<int:id>/', views.car_delete, name='car_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
